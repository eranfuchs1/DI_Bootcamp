from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bookings, ContactUs


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class BookingForm(ModelForm):
    check_in_date = forms.DateField(widget=forms.SelectDateWidget)
    check_out_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Bookings
        exclude = ['guest', 'approved']


class ContactUsFormForUser(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['text', ]


class ContactUsFormForNonUser(ModelForm):
    class Meta:
        model = ContactUs
        exclude = ['guest', ]
