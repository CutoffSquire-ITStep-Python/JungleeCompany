from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('locations/', include('locations.urls')),
    path('api/', include('api.urls')),
]

handler404 = 'core.views.custom_404_view'