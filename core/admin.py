from django.contrib import admin
from .models import New, Employee

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'initials', 'role']