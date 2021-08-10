from django.shortcuts import render, redirect
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
        "passengers": flight.passengers.all(),
        "non_passenger": models.Passenger.objects.exclude(flight=flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = models.Flight.objects.get(pk=flight_id)
        passenger = models.Passenger.objects.get(pk=int(request.POST["passenger"]))

        passenger.flight.add(flight)

        return redirect('flights', flight_id=flight_id)


