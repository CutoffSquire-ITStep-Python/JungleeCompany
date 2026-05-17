from django.urls import path
from api.views import ApiGetView

urlpatterns = [
    path('api/', ApiGetView.as_view(), name='api'),
]