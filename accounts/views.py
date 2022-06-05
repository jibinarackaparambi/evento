from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

from .forms import UserForm

# Create your views here.


class SignUpView(CreateView):
    model = UserForm
    form_class = UserForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')
