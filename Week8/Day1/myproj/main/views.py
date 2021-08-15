from django.shortcuts import render, HttpResponse
# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('about page')
