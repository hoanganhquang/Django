from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flights, name="flights"),
    path("passengers/<int:passenger_id>", views.passengers, name="passengers")
]

