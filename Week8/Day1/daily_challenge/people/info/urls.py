from django.urls import path
from .views import people

urlpatterns = [
        path('', people),
        path('<int:X>', people),
]
