from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserSignupForm, BookingForm, ContactUsFormForNonUser, ContactUsFormForUser
from .models import Bookings
from .vacancies import day_is_vacancy, get_bookings, get_vacancies, is_vacancy, is_valid_check_in_out_dates
from django.views.generic.edit import CreateView
from django.contrib.messages import add_message
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class SignupView(CreateView):
    form_class = UserSignupForm
    template_name = 'signup.html'
    success_url = 'login'


class BookingView(LoginRequiredMixin, CreateView):
    form_class = BookingForm
    template_name = 'booking.html'

    def form_valid(self, form, **kwargs):
        if is_valid_check_in_out_dates(form.cleaned_data['check_in_date'], form.cleaned_data['check_out_date']):
            if is_vacancy(form.cleaned_data['room'], form.cleaned_data['check_in_date'], form.cleaned_data['check_out_date']):
                booking = Bookings(**form.cleaned_data,
                                   guest=self.request.user)
                booking.save()
                add_message(self.request, messages.SUCCESS,
                            'booking added successfully')
                return redirect('homepage')
            else:
                add_message(self.request, messages.ERROR,
                            'invalid date range for this room, sorry, this room is already booked for the chosen dates')
                return redirect('booking')
        else:
            add_message(self.request, messages.ERROR,
                        'invalid date range')
            return redirect('booking')


def vacancies_view(request, room_number):
    context = {}
    context['vacancies'] = get_vacancies(
        room_number=room_number)
    context['bookings'] = get_bookings(room_number)
    return render(request, 'vacancies.html', context=context)


class ContactUsViewUser(LoginRequiredMixin, CreateView):
    form_class = ContactUsFormForUser
    template_name = 'contact_us.html'
    success_url = reverse_lazy('homepage')


class ContactUsViewNonUser(CreateView):
    form_class = ContactUsFormForNonUser
    template_name = 'contact_us.html'
    success_url = reverse_lazy('homepage')


def homepage_view(request):
    return render(request, 'about.html', context={})
