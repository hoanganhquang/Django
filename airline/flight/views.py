from django.shortcuts import render
from . import models


def index(request):
    return render(request, "flight/index.html", {
        "flights": models.Flight.objects.all(),
        "airports": models.Airport.objects.all()
    })


def flights(request, flight_id):
    flight = models.Flight.objects.get(pk=flight_id)
    return render(request, "flight/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })


def passengers(request, passenger_id):
    passenger = models.Passenger.objects.get(pk=passenger_id)
    return render(request, "flight/passenger.html", {
        "passenger": passenger
    })
