from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, profile, logout_view


urlpatterns = [
    #path('homepage/', view_placeholder, 'homepage'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
]
