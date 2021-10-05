from django.urls import path
from .views import SignupView, BookingView, ContactUsViewUser, ContactUsViewNonUser, homepage_view

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('contact_us/user/', ContactUsViewUser.as_view(), name='contact_us_user'),
    path('contact_us/nonuser/', ContactUsViewNonUser.as_view(),
         name='contact_us_nonuser'),
    path('', homepage_view, name='homepage'),
]
