from django.urls import path
from .views import customer_view, rental_view, vehicle_view, customer_add_view, rental_add_view, vehicle_add_view

urlpatterns = [
    path('rental/add'        , rental_add_view               ),
    path('vehicle/add'       , vehicle_add_view              ),
    path('customer/add'      , customer_add_view             ),
    path('rental/'           , rental_view, name='rental'    ),
    path('rental/<int:pk>'   , rental_view                   ),
    path('vehicle/'          , vehicle_view, name='vehicle'  ),
    path('vehicle/<int:pk>'  , vehicle_view                  ),
    path('customer/'         , customer_view, name='customer'),
    path('customer/<int:pk>' , customer_view                 ),
]
