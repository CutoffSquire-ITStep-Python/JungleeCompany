from django.urls import path, re_path
from django.http import Http404
from . import views

def news_404(request, *args, **kwargs):
    raise Http404('Сторінку в розділі Новини не знайдено')

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/create/', views.news_create, name='news_create'),
    re_path(r'^news/.+$', news_404),
    path('management/', views.management, name='management'),
    path('management/create/', views.management_create, name='management_create'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]