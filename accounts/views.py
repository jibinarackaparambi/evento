from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from .forms import UserForm

# Create your views here.


class SignUpView(CreateView):
    model = UserForm
    form_class = UserForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        messages.success(self.request, "Your account successfully created.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('signup')
