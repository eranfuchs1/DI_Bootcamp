from django.urls import path
from .views import animal_view, animals_view, family_view

urlpatterns = [
    path('family/<int:X>', family_view),
    path('animal/<int:X>', animal_view),
    path('animals/', animals_view),
]
