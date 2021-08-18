from django.db import models

# Create your models here.
class Gif(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField()
    uploader_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=80)
    gifs = models.ManyToManyField(Gif)
