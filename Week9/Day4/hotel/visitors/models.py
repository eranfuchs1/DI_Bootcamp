from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Bookings(models.Model):
    guest = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    room = models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(1)])
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    approved = models.BooleanField(default=False)


class ContactUs(models.Model):
    guest = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    email = models.EmailField(null=True)
    first_name = models.CharField(max_length=80, null=True)
    last_name = models.CharField(max_length=80, null=True)
    text = models.TextField()