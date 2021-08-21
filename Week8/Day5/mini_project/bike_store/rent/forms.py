from django import forms

class RentalAdd(forms.Form):
    customer_id     = forms.IntegerField()
    vehicle_id      = forms.IntegerField()


class CustomerAdd(forms.Form):
    first_name      = forms.CharField(max_length=80)
    last_name       = forms.CharField(max_length=80)
    email           = forms.CharField(max_length=300)
    phone_number    = forms.CharField(max_length=20)
    address         = forms.CharField(max_length=300)
    city            = forms.CharField(max_length=80)
    country         = forms.CharField(max_length=80)

class VehicleAdd(forms.Form):
    vehicle_type_id = forms.IntegerField()
    cost            = forms.IntegerField()
    size_id         = forms.IntegerField()
