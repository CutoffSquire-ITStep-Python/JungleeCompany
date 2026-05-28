from django.views import View
from django.http import JsonResponse
from django.shortcuts import render

from data.news import NEWS
from data.management import MANAGEMENT


class ApiGetView(View):

    def dispatch(self, request, *args, **kwargs):
        action = request.GET.get('action', 'default')

        if action == 'news':
            return self.handle_news(request)
        elif action == 'management':
            return self.handle_management(request)
        else:
            return self.handle_default(request)

    def handle_news(self, request):
        return JsonResponse(NEWS, json_dumps_params={'ensure_ascii': False}, safe=False)

    def handle_management(self, request):
        return JsonResponse(MANAGEMENT, json_dumps_params={'ensure_ascii': False}, safe=False)

    def handle_default(self, request):
        return render(request, 'api/index.html', {'title': 'АПI'})