from django.urls import path
from django.contrib.auth.views import LoginView

from .views import SignUpView

urlpatterns = [
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup', SignUpView.as_view(), name='signup'),
]
