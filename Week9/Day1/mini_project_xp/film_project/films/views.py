from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic.list import ListView
from .forms import AddDirectorForm, AddFilmForm
from .models import Film
# Create your views here.

class AddDirectorView(FormView):
    form_class = AddDirectorForm
    template_name = 'director/add_directory.html'
    def post(self, request, *args, **kwargs):
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')




class AddFilmView(FormView):
    form_class = AddFilmForm
    template_name = 'film/add_film.html'
    def post(self, request, *args, **kwargs):
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')


class HomepageView(ListView):
    model = Film
    template_name = 'homepage.html'
