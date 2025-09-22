
from django.shortcuts import render, get_object_or_404
from .models import Car

def products(request):
    query = request.GET.get('search', '')
    if query:
        cars = Car.objects.filter(name__icontains=query)
    else:
        cars = Car.objects.all()
    return render(request, 'core/cars.html', {'cars': cars, 'search': query})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    daily = car.daily or 0
    weekly = car.weekly or 0
    monthly = car.monthly or 0
    yearly = car.yearly or 0
    daily7 = daily * 7
    daily30 = daily * 30
    daily365 = daily * 365
    monthly_discount = daily30 - monthly
    yearly_discount = daily365 - yearly
    weekly_discount = daily7 - weekly
    return render(request, 'core/car_detail.html', {
        'car': car,
        'daily7': daily7,
        'weekly_discount': weekly_discount,
        'daily30': daily30,
        'monthly_discount': monthly_discount,
        'daily365': daily365,
        'yearly_discount': yearly_discount,
    })