from django.shortcuts import render

from data.news import NEWS
from data.management import MANAGEMENT


def home(request):
    return render(request, 'index.html', {'title': 'Головна'})

def news(request):
    return render(request, 'news.html', {'title': 'Новини', "news": NEWS})

def management(request):
    return render(request, 'management.html', {'title': 'Керівництво компанії', "management": MANAGEMENT})

def about(request):
    return render(request, 'about.html', {'title': 'Про компанію'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Контакти'})