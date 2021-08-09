from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=10)
    city = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"


class Passenger(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    flight = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.fname} {self.lname}"
