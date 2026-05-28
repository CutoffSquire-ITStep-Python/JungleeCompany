from django.urls import path
from locations.views import LocationListView, LocationCreateView, GuardianCreateView

urlpatterns = [
    path('', LocationListView.as_view(), name='locations'),
    path('create/', LocationCreateView.as_view(), name='location_create'),
    path('guardians/create/', GuardianCreateView.as_view(), name='guardian_create'),
]