from django.shortcuts import render,get_object_or_404
from .models import car

# Create your views here.

def cars(request):
    cars = car.objects.order_by('-created_date')
    data = {
        'cars': cars,
    }
    return render(request, 'cars/cars.html',data)

def car_detail(request,id):
    single_car = get_object_or_404(car, pk=id)
    #get primary key , get data from datebase, if data not available then return 404

    data = {
        'single_car' : single_car,
    }
    return render(request,'cars/car_detail.html',data)

def search(request):
    cars =car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__iexact=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(City__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price =request.GET['min_price']
        max_price =request.GET['max_price']
        if max_price:
            cars= cars.filter(price_gte=min_price, price_lte=max_price)

    data={
        'cars' : cars,
    }
    return render(request,'cars/search.html',data)
