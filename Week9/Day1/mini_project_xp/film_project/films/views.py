from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import FormView, DeleteView
from django.views.generic.list import ListView
from .forms import AddDirectorForm, AddFilmForm, CommentFilmForm, RateFilmForm
from .models import Film, Director, FilmComment, FilmRate
# Create your views here.


class SuperUserForm:
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        return redirect('homepage')

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().delete(request, args, kwargs)
        return redirect('homepage')


class AddDirectorView(SuccessMessageMixin, SuperUserForm, FormView):
    form_class = AddDirectorForm
    template_name = 'director/add_directory.html'
    success_message = 'director was added successfully'


class DeleteDirectorView(SuperUserForm, SuccessMessageMixin, DeleteView):
    model = Director
    template_name = 'director/delete_director.html'
    success_message = 'director {} was deleted successfully'
    success_url = reverse_lazy('homepage')

    def get_success_message(self):
        return self.success_message.format(self.get_object())

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.get_success_message())
        return super(DeleteDirectorView, self).delete(request, *args, **kwargs)


class DeleteFilmView(SuperUserForm, SuccessMessageMixin, DeleteView):
    model = Film
    template_name = 'director/delete_director.html'
    success_message = 'film {} was deleted successfully'
    success_url = reverse_lazy('homepage')

    def get_success_message(self):
        return self.success_message.format(self.get_object())

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.get_success_message())
        return super(DeleteFilmView, self).delete(request, *args, **kwargs)


class AddFilmView(SuccessMessageMixin, SuperUserForm, FormView):
    form_class = AddFilmForm
    template_name = 'film/add_film.html'
    success_message = 'film was added successfully'


class CommentFilmView(FormView):
    form_class = CommentFilmForm
    template_name = 'film/add_film.html'
    success_url = reverse_lazy('homepage')
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            f = Film.objects.get(id=kwargs['id'])
            c = FilmComment.objects.create(user=self.request.user, comment=self.request.POST.get('comments'))
            f.comments.add(c)
            f.save()
        return redirect('homepage')


class HomepageView(ListView):
    model = Film
    template_name = 'homepage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentFilmForm()
        context['rate_form'] = RateFilmForm()
        return context

class DirectorListView(ListView):
    model = Director
    template_name = 'delete_director.html'
