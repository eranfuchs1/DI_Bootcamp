from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)

class Category(models.Model):
    name = models.CharField(max_length=80)

class Director(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

class Film(models.Model):
    title = models.CharField(max_length=80)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
    available_in_countries = models.ManyToManyField(Country)
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)
