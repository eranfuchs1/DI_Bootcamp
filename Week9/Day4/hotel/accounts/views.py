from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'homepage'
    def get_success_url(self):
        return reverse_lazy(self.success_url)