from django.urls import path
from .views import homepage, about

urlpatterns = [
        path('', homepage),
        path('about', about),
]
