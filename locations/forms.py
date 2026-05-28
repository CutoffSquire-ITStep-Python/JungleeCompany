import os
from datetime import datetime, timedelta
from django import forms
from .models import Location, Guardian

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description', 'is_portal_open', 'guardian', 'work_starts_at', 'finish_work_at', 'secret_password', 'image']
        labels = {
            'name': "Назва",
            'description': "Опис",
            'is_portal_open': "Портал відкритий",
            'guardian': "Сторож",
            'work_starts_at': "Час початку роботи",
            'finish_work_at': "Час завершення роботи",
            'secret_password': "Таємний пароль",
            'image': "Зображення",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва локації'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис локації'}),
            'is_portal_open': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'guardian': forms.Select(attrs={'class': 'form-control'}),
            'work_starts_at': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'finish_work_at': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'secret_password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Таємний пароль (10-20 літер)'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'image': "Дозволено: JPG, JPEG, PNG (максимум 5 МБ)",
        }
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return image
    
        ext = os.path.splitext(image.name)[1].lower()
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if ext not in valid_extensions:
            raise forms.ValidationError("Дозволені тільки формати: JPG, JPEG, PNG")
    
        if image.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Фото занадто велике. Максимальний розмір — 5 МБ.")
        return image

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('work_starts_at')
        finish = cleaned_data.get('finish_work_at')

        if start and finish:
            today = datetime.today().date()
            start_dt = datetime.combine(today, start)
            finish_dt = datetime.combine(today, finish)

            if finish_dt <= start_dt:
                finish_dt += timedelta(days=1)

            duration = finish_dt - start_dt

            if duration < timedelta(hours=1):
                raise forms.ValidationError(
                    "Зміна повинна тривати щонайменше 1 годину."
                )

        return cleaned_data

class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ['name']
        labels = { 'name': "Ім'я" }
        widgets = { 'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ім\'я сторожа'}) }