import json
from .models import Event
from .forms import EventForm

from django.views.generic import ListView
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
class EventSerchView(ListView):
    def get(self, request, *args, **kwargs):
        result = []
        if 'term' in request.GET:
            query = Event.objects.filter(name__istartswith=request.GET.get('term'))
            result = [{ "label": r.name, "value": r.name} for r in query]
            if len(result) == 0:
                result.clear()
                result = [{ "label": "No data found", "value": ""}]
            return JsonResponse(result, safe=False)

        return render(request, 'evento/home.html')


class HomeView(ListView):
    model = Event
    template_name = 'evento/home.html'
    context_object_name = 'events'
    # form_class = EventForm
