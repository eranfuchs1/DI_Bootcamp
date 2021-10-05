from django.urls import path
from .views import CustomLoginView as LoginView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]