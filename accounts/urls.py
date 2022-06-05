from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login')
]
