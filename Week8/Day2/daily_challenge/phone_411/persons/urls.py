from django.urls import path
from .views import by_name, by_phonenumber

urlpatterns = [
    path('name/<str:name>', by_name),
    path('phonenumber/<str:num>', by_phonenumber),
]
