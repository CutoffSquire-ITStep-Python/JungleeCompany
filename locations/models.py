import os
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from datetime import datetime

class Guardian(models.Model):
    name = models.CharField("Ім'я", unique=True, max_length=50, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = "Сторож"
        verbose_name_plural = "Сторожі"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

def image_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    new_name = f"location_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
    return f'locations/{new_name}'

class Location(models.Model):
    name = models.CharField("Назва", max_length=100, validators=[MinLengthValidator(3)])
    secret_password = models.CharField("Секретний пароль", max_length=20, blank=True, null=True, validators=[MinLengthValidator(10), RegexValidator(regex=r'^[а-яА-Я]{10,20}$')])
    description = models.TextField("Опис", blank=True)
    is_portal_open = models.BooleanField("Портал відчинений", default=True)

    work_starts_at = models.TimeField("Дата початку роботи")
    finish_work_at = models.TimeField("Дата завершення роботи")

    image = models.ImageField("Фото", upload_to=image_upload_path, blank=True, null=True)

    guardian = models.ForeignKey(
        Guardian,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='locations',
        verbose_name="Сторож"
    )

    class Meta:
        verbose_name = "Локація"
        verbose_name_plural = "Локації"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"