from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class VehicleType(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return str(self.name)

class VehicleSize(models.Model):
    size = models.IntegerField()
    def __str__(self):
        return str(self.size)

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    cost = models.IntegerField()
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

class Rental(models.Model):
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    vehicle =  models.ForeignKey(VehicleSize, on_delete=models.DO_NOTHING)


class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
