from django.urls import path
from .views import AddDirectorView, AddFilmView, HomepageView

urlpatterns = [
    #path('homepage/', view_placeholder, 'homepage'),
    path('add_director/', AddDirectorView.as_view(), name='add_director'),
    path('add_film/', AddFilmView.as_view(), name='add_film'),
    path('homepage/', HomepageView.as_view(), name='homepage'),
]
