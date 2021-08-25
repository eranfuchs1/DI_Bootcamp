from django.urls import path
from .views import AddDirectorView, AddFilmView, HomepageView, DeleteDirectorView, DeleteFilmView, DirectorListView, CommentFilmView

urlpatterns = [
    #path('homepage/', view_placeholder, 'homepage'),
    path('add_director/', AddDirectorView.as_view(), name='add_director'),
    path('delete_director/<int:pk>', DeleteDirectorView.as_view(), name='delete_director'),
    path('delete_film/<int:pk>', DeleteFilmView.as_view(), name='delete_film'),
    path('add_film/', AddFilmView.as_view(), name='add_film'),
    path('homepage/', HomepageView.as_view(), name='homepage'),
    path('directors_list/', DirectorListView.as_view(), name='directors_list'),
    path('comment_film/<int:id>', CommentFilmView.as_view(), name='comment_film'),
]
