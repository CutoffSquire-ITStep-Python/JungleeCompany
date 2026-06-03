from django.db import models
from django.core.validators import MinLengthValidator

class Employee(models.Model):
    ROLE_CHOICES = [
        ('none', 'Unnamed Employee'),
        ('general_director', 'Генеральний директор'),
        ('technical_director', 'Технічний директор'),
        ('finance_director', 'Фінансовий директор'),
        ('main_architect', 'Головний архітектор'),
    ]

    full_name = models.CharField('Ім\'я', max_length=150, validators=[MinLengthValidator(3)])
    initials = models.CharField('Ініціали', max_length=2, validators=[MinLengthValidator(2)])
    description = models.CharField('Опис', max_length=250, null=False, blank=False)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='none',
        verbose_name="Роль"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Роботник"
        verbose_name_plural = "Роботник"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

class New(models.Model):
    title = models.CharField("Назва", blank=True, max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField("Опис", blank=True)

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новина"
        ordering = ['-publish_date', 'title']

    def __str__(self):
        return f"{self.title}"