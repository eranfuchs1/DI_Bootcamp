from django.shortcuts import render
from .models import Animal, Family

# Create your views here.
def animal_view(request, X):
    context = {}
    animal = Animal.objects.get(id=X)
    context['animal'] = animal
    return render(request, 'animal.html', context)
def family_view(request, X):
    context = {}
    family = Family.objects.get(id=X)
    context['family'] = family
    animals = Animal.objects.filter(family=family)
    context['animals'] = animals
    return render(request, 'family.html', context)
def animals_view(request):
    context = {}
    animals = Animal.objects.all()
    context['animals'] = animals
    return render(request, 'animals.html', context)
