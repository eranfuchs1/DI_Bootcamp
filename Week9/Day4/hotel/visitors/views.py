from django.shortcuts import render
from .forms import UserSignupForm
from django.views.generic.edit import CreateView

# Create your views here.

class SignupView(CreateView):
    form_class = UserSignupForm
    template_name = 'signup.html'