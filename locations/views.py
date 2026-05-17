from asgiref.sync import sync_to_async
from django.views.generic import ListView
import asyncio
import time

from data.locations import LOCATIONS


class LocationListView(ListView):
    template_name = "locations/index.html"
    context_object_name = "locations"

    def get_queryset(self):
        return LOCATIONS

    async def get_context_data(self, **kwargs):
        context = await sync_to_async(super().get_context_data)(**kwargs)

        await asyncio.sleep(0.1)

        context["updated_at"] = time.strftime("%H:%M:%S")
        context["title"] = 'Локації'
        return context

    async def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = await self.get_context_data(**kwargs)
        return await sync_to_async(self.render_to_response)(context)