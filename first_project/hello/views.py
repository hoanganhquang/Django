from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def home(request, name):
    return render(request, "home.html", {
        "name": name.capitalize()
    })
