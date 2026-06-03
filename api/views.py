from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from core.views import render

from core.models import New, Employee
from locations.models import Location, Guardian

def home(request):
    return render(request, 'api/index.html', {'title': 'АПI'})

# -~==%&&%==~- NEWS -~==%&&%==~-
@api_view(['GET'])
def news_list(request):
    """GET /api/news/ - Список усіх новин"""
    news = New.objects.all()
    data = [{
        'id': n.id,
        'title': n.title,
        'content': n.content,
        'publish_date': n.publish_date,
    } for n in news]
    return Response(data)

@api_view(['GET', 'POST'])
def news_detail(request, pk):
    """GET /api/news/{id}/  
       POST /api/news/{id}/ (оновлення)"""
    news = get_object_or_404(New, pk=pk)

    if request.method == 'GET':
        data = {
            'id': news.id,
            'title': news.title,
            'content': news.content,
            'publish_date': news.publish_date,
        }
        return Response(data)

    if request.method == 'POST':
        if not request.user.is_staff:
            return Response({"detail": "Доступ заборонено"}, status=status.HTTP_403_FORBIDDEN)
        
        news.title = request.data.get('title', news.title)
        news.content = request.data.get('content', news.content)
        news.save()
        return Response({"detail": "Новину оновлено"})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def news_create(request):
    """POST /api/news/ - створення нової новини"""
    serializer_data = {
        'title': request.data.get('title'),
        'content': request.data.get('content', ''),
    }
    news = New.objects.create(**serializer_data)
    return Response({
        'id': news.id,
        'title': news.title,
        'message': 'Новину успішно створено'
    }, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def news_delete(request, pk):
    """DELETE /api/news/{id}/ - видалення новини"""
    news = get_object_or_404(New, pk=pk)

    news.delete()
    return Response({"detail": "Новину видалено"})


# -~==%&&%==~- EMPLOYEES -~==%&&%==~-
@api_view(['GET'])
def employee_list(request):
    """GET /api/employees/ - Список усіх співробітників"""
    employees = Employee.objects.all()
    data = [{
        'id': e.id,
        'full_name': e.full_name,
        'initials': e.initials,
        'description': e.description,
        'role': e.get_role_display(),
    } for e in employees]
    return Response(data)

@api_view(['GET', 'POST'])
def employee_detail(request, pk):
    """GET /api/employees/{id}/  
       POST /api/employees/{id}/ (оновлення)"""
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'GET':
        data = {
            'id': employee.id,
            'full_name': employee.full_name,
            'initials': employee.initials,
            'description': employee.description,
            'role': employee.get_role_display(),
        }
        return Response(data)

    if request.method == 'POST':
        if not request.user.is_staff:
            return Response({"detail": "Доступ заборонено"}, status=status.HTTP_403_FORBIDDEN)
        
        employee.full_name = request.data.get('full_name', employee.full_name)
        employee.initials = request.data.get('initials', employee.initials)
        employee.description = request.data.get('description', employee.description)
        employee.role = request.data.get('role', employee.role)
        employee.save()
        return Response({"detail": "Співробітника оновлено"})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def employee_create(request):
    """POST /api/employees/ - створення нового співробітника"""
    serializer_data = {
        'full_name': request.data.get('full_name'),
        'initials': request.data.get('initials'),
        'description': request.data.get('description'),
        'role': request.data.get('role'),
    }
    employee = Employee.objects.create(**serializer_data)
    return Response({
        'id': employee.id,
        'full_name': employee.full_name,
        'initials': employee.initials,
        'description': employee.description,
        'role': employee.get_role_display(),
        'message': 'Співробітника успішно створено'
    }, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def employee_delete(request, pk):
    """DELETE /api/employees/{id}/ - видалення співробітника"""
    employee = get_object_or_404(Employee, pk=pk)

    employee.delete()
    return Response({"detail": "Співробітника видалено"})


# -~==%&&%==~- LOCATIONS -~==%&&%==~-
@api_view(['GET'])
def location_list(request):
    """GET /api/locations/ - Список усіх локацій"""
    locations = Location.objects.select_related('guardian').all()
    data = [{
        'id': l.id,
        'name': l.name,
        'secret_password': l.secret_password,
        'description': l.description,
        'is_portal_open': l.is_portal_open,
        'work_starts_at': l.work_starts_at,
        'finish_work_at': l.finish_work_at,
        'guardian_id': l.guardian.id if l.guardian else None,
    } for l in locations]
    return Response(data)

@api_view(['GET', 'POST'])
def location_detail(request, pk):
    """GET /api/locations/{id}/  
       POST /api/locations/{id}/ (оновлення)"""
    location = get_object_or_404(Location, pk=pk)

    if request.method == 'GET':
        data = {
            'id': location.id,
            'name': location.name,
            'secret_password': location.secret_password,
            'description': location.description,
            'is_portal_open': location.is_portal_open,
            'work_starts_at': location.work_starts_at,
            'finish_work_at': location.finish_work_at,
            'guardian_id': location.guardian.id if location.guardian else None,
        }
        return Response(data)

    if request.method == 'POST':
        if not request.user.is_staff:
            return Response({"detail": "Доступ заборонено"}, status=status.HTTP_403_FORBIDDEN)
        
        location.name = request.data.get('name', location.name)
        location.secret_password = request.data.get('secret_password', location.secret_password)
        location.description = request.data.get('description', location.description)
        location.is_portal_open = request.data.get('is_portal_open', location.is_portal_open)
        location.work_starts_at = request.data.get('work_starts_at', location.work_starts_at)
        location.finish_work_at = request.data.get('finish_work_at', location.finish_work_at)
        location.save()
        return Response({"detail": "Локацію оновлено"})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def location_create(request):
    """POST /api/locations/ - створення нової локації"""
    serializer_data = {
        'name': request.data.get('name'),
        'secret_password': request.data.get('secret_password'),
        'description': request.data.get('description'),
        'is_portal_open': request.data.get('is_portal_open'),
        'work_starts_at': request.data.get('work_starts_at'),
        'finish_work_at': request.data.get('finish_work_at'),
        'guardian': request.data.get('guardian'),
    }
    location = Location.objects.create(**serializer_data)
    return Response({
        'id': location.id,
        'name': location.name,
        'message': 'Локацію успішно створено'
    }, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def location_delete(request, pk):
    """DELETE /api/locations/{id}/ - видалення локації"""
    location = get_object_or_404(Location, pk=pk)

    location.delete()
    return Response({"detail": "Локацію видалено"})


# -~==%&&%==~- GUARDIANS -~==%&&%==~-
@api_view(['GET'])
def guardian_list(request):
    """GET /api/guardians/ - Список усіх охоронців"""
    guardians = Guardian.objects.all()
    data = [{
        'id': g.id,
        'name': g.name,
    } for g in guardians]
    return Response(data)

@api_view(['GET', 'POST'])
def guardian_detail(request, pk):
    """GET /api/guardians/{id}/  
       POST /api/guardians/{id}/ (оновлення)"""
    guardian = get_object_or_404(Guardian, pk=pk)

    if request.method == 'GET':
        data = {
            'id': guardian.id,
            'name': guardian.name,
        }
        return Response(data)

    if request.method == 'POST':
        if not request.user.is_staff:
            return Response({"detail": "Доступ заборонено"}, status=status.HTTP_403_FORBIDDEN)
        
        guardian.name = request.data.get('name', guardian.name)
        guardian.save()
        return Response({"detail": "Охоронця оновлено"})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def guardian_create(request):
    """POST /api/guardians/ - створення нового охоронця"""
    serializer_data = {
        'name': request.data.get('name'),
    }
    guardian = Guardian.objects.create(**serializer_data)
    return Response({
        'id': guardian.id,
        'name': guardian.name,
        'message': 'Охоронця успішно створено'
    }, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def guardian_delete(request, pk):
    """DELETE /api/guardians/{id}/ - видалення охоронця"""
    guardian = get_object_or_404(Guardian, pk=pk)

    guardian.delete()
    return Response({"detail": "Охоронця видалено"})

