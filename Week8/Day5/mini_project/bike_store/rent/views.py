from django.shortcuts import render, HttpResponse, redirect
from .models import Customer, Rental, RentalRate, Vehicle, VehicleSize, VehicleType
from .forms import CustomerAdd, RentalAdd, VehicleAdd

# Create your views here.
def rental_view(request, pk=None):
    context = {}
    if pk:
        try:
            context['rental'] = Rental.objects.get(id=pk)
            return render(request, 'rental.html', context=context)
        except:
            return HttpResponse(f'no rental exists with the given id of {pk}')
    else:
        context['rentals'] = Rental.objects.all()
        return render(request, 'rental_all.html', context=context)





def customer_view(request, pk=None):
    context = {}
    if pk:
        try:
            context['customer'] = Customer.objects.get(id=pk)
            return render(request, 'customer.html', context=context)
        except:
            return HttpResponse(f'no customer exists with the given id of {pk}')
    else:
        context['customers'] = Customer.objects.all()
        return render(request, 'customer_all.html', context=context)



def vehicle_view(request, pk=None):
    context = {}
    if pk:
        try:
            context['vehicle'] = Vehicle.objects.get(id=pk)
            return render(request, 'vehicle.html', context=context)
        except:
            return HttpResponse(f'no vehicle exists with the given id of {pk}')
    else:
        #context['vehicles'] = Vehicle.objects.all()
        vehicles = Vehicle.objects.all()
        groups = {}
        for vehicle in vehicles:
            if vehicle.vehicle_type.name in groups:
                groups[vehicle.vehicle_type.name].append(vehicle)
            else:
                groups[vehicle.vehicle_type.name] = []
                groups[vehicle.vehicle_type.name].append(vehicle)
        context['groups'] = [{'name':key,'vehicles':groups[key]} for key in groups]
        return render(request, 'vehicles_by_groups.html', context=context)


def _add_view(request, form_cls, model_cls, name):
    context = {}
    if   request.method == 'GET':
        context['form'] = form_cls()
        return render(request, 'add.html', context=context)
    elif request.method == 'POST':
        form = form_cls(request.POST)
        if form.is_valid():
            r = model_cls.objects.create(**form.cleaned_data)
            r.save()
    return redirect(name)

def rental_add_view(request):
    return _add_view(request, RentalAdd, Rental, 'rental')

def vehicle_add_view(request):
    return _add_view(request, VehicleAdd, Vehicle, 'vehicle')

def customer_add_view(request):
    return _add_view(request, CustomerAdd, Customer, 'customer')
