from django.shortcuts import redirect, render
from django.contrib import messages
from core.forms import EmployeeForm, NewForm

from .models import New, Employee


def home(request):
    return render(request, 'index.html', {'title': 'Головна'})

def news(request):
    return render(request, 'news.html', {'title': 'Новини', "news": New.objects.all()})

def news_create(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, 'Новина успішно надіслана та збережена!')
            return redirect('news')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = NewForm()

    return render(request, 'news_form.html', {
        'form': form,
        'title': 'Відправка новини',
    })

def management(request):
    return render(request, 'management.html', {'title': 'Керівництво компанії', "management": Employee.objects.all()})

def management_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, 'Роботник успішно надісланий та збережений!')
            return redirect('management')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = EmployeeForm()

    return render(request, 'management_form.html', {
        'form': form,
        'title': 'Створення роботника',
    })

def about(request):
    return render(request, 'about.html', {'title': 'Про компанію'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Контакти'})


def custom_404_view(request, exception):
    message = str(exception) if str(exception) else 'Сторінку не знайдено'
    return render(request, '404.html', {'message': message}, status=404)