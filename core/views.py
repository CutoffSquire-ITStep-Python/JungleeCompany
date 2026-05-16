from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'title': 'Головна'})

def news(request):
    return render(request, 'news.html', {'title': 'Новини'})

def management(request):
    return render(request, 'management.html', {'title': 'Керівництво компанії'})

def about(request):
    return render(request, 'about.html', {'title': 'Про компанію'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Контакти'})