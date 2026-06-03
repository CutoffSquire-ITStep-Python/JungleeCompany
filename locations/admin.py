from django.contrib import admin
from .models import Location, Guardian

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_portal_open']

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ['name']