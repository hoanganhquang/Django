from django.shortcuts import render
from . import models


def index(request):
    return render(request, "flight/index.html", {
        "flights": models.Flight.objects.all()
    })
