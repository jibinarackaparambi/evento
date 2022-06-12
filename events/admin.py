from .models import Event
from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Event, EventAdmin)