from django.shortcuts import render
from .models import Person

# Create your views here.
def by_phonenumber(request, num):
    context = {}
    try:
        person = Person.objects.get(phone_number=num)
    except:
        person = None
    context['person'] = person
    context['detail'] = 'phone number'
    context['detail_data'] = num
    return render(request, 'person_details.html', context=context)


def by_name(request, name):
    context = {}
    try:
        person = Person.objects.get(name=name)
    except:
        person = None
    context['person'] = person
    context['detail'] = 'name'
    context['detail_data'] = name
    return render(request, 'person_details.html', context=context)
