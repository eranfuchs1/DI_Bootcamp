from django.forms import ModelForm
from django import forms
from .models import Category, Country, Director, Film, FilmComment, FilmRate

class AddFilmForm(ModelForm):
    class Meta:
        model = Film
        exclude = ['comments', 'rate']

class AddDirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'


class CommentFilmForm(forms.Form):
    comments = forms.CharField(widget=forms.Textarea)

class RateFilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['rate']