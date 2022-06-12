
from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=132)
    location_name = models.CharField(max_length=132)
    date = models.DateTimeField()
    time = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0.0)
    img = models.ImageField(blank=True,null=True)