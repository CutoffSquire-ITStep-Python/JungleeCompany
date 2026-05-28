from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
import time

from .models import Location, Guardian
from .forms import LocationForm, GuardianForm


class LocationListView(ListView):
    model = Location
    template_name = "locations/index.html"
    context_object_name = "locations"

    def get_queryset(self):
        locations = Location.objects.select_related('guardian').all()
        for location in locations:
            if not location.is_portal_open:
                location.portal_status = "Зачинений на обід"
            else:
                location.portal_status = "Відкритий"
        return locations

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["updated_at"] = time.strftime("%H:%M:%S")
        context["title"] = 'Локації'
        return context


class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = "locations/location_form.html"
    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Додавання локації"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Локацію успішно додано!")
        return super().form_valid(form)


class GuardianCreateView(CreateView):
    model = Guardian
    form_class = GuardianForm
    template_name = "locations/guardian_form.html"
    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Додавання сторожа"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Сторожа успішно додано!")
        return super().form_valid(form)