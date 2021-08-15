from django.urls import path
from .views import animal, family

urlpatterns = [
        path('animal/<int:X>', animal),
        path('family/<int:X>', family),
]
