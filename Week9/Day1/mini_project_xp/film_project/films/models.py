from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FilmComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_created')
    comment = models.TextField()
    def __str__(self):
        return f"{self.user.username}: {self.comment}"



class FilmRate(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_created')
    rate = models.TextField()

class Film(models.Model):
    title = models.CharField(max_length=80)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey(
        Country, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_created')
    comments = models.ManyToManyField(FilmComment, null=True)
    rate = models.ManyToManyField(FilmRate, null=True)
    available_in_countries = models.ManyToManyField(Country)
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)
    def __str__(self):
        return self.title
