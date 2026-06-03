from django import forms
from .models import New, Employee

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'content']
        labels = {
            'title': "Назва",
            'content': "Опис",
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва новини'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис новини'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'initials', 'description', 'role']
        labels = {
            'full_name': "Ім'я",
            'initials': "Ініціали",
            'description': "Опис",
            'role': "Роль",
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ім\'я працівника'}),
            'initials': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ініціали працівника'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис працівника'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }