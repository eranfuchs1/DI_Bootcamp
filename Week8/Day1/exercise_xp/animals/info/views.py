from django.shortcuts import render
from .read_json import read_json_animal, read_json_family

# Create your views here.
def family(request, X):
    context = {}
    context['data'] = read_json_family(X)
    return render(request, 'family.html', context)

def animal(request, X):
    context = {}
    context['data'] = read_json_animal(X)
    return render(request, 'animal.html', context)
