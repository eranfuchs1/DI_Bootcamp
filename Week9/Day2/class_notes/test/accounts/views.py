from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
