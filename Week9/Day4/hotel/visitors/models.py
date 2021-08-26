from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Rooms(models.Model):
    room_number = models.IntegerField()


class Bookings(models.Model):
    guest = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Rooms, on_delete=models.DO_NOTHING)
    check_in_date = models.DateField(auto_now_add=True)
    check_out_date = models.DateField()
