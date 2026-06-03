from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='api'),

    # -~==%&&%==~- NEWS -~==%&&%==~-
    path('news/', views.news_list, name='api/news'),
    path('news/create/', views.news_create, name='api/news/create'),
    path('news/<int:pk>/', views.news_detail, name='api/news/detail'),
    path('news/delete/<int:pk>/', views.news_delete, name='api/news/delete'),

    
    # -~==%&&%==~- EMPLOYEES -~==%&&%==~-
    path('employees/', views.employee_list, name='api/employees'),
    path('employees/create/', views.employee_create, name='api/employees/create'),
    path('employees/<int:pk>/', views.employee_detail, name='api/employees/detail'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='api/employees/delete'),

    # -~==%&&%==~- LOCATIONS -~==%&&%==~-
    path('locations/', views.location_list, name='api/locations'),
    path('locations/create/', views.location_create, name='api/locations/create'),
    path('locations/<int:pk>/', views.location_detail, name='api/locations/detail'),
    path('locations/delete/<int:pk>/', views.location_delete, name='api/locations/delete'),

    # -~==%&&%==~- GUARDIANS -~==%&&%==~-
    path('guardians/', views.guardian_list, name='api/guardians'),
    path('guardians/create/', views.guardian_create, name='api/guardians/create'),
    path('guardians/<int:pk>/', views.guardian_detail, name='api/guardians/detail'),
    path('guardians/delete/<int:pk>/', views.guardian_delete, name='api/guardians/delete'),
]