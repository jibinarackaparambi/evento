from django.urls import path
from .views import *

urlpatterns = [
    path('search/', EventSerchView.as_view(), name='search'),
    path('', HomeView.as_view(), name='home'),
]
