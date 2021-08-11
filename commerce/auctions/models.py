from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListings(models.Model):
    item_name = models.CharField(max_length=20)
    price = models.FloatField()
    seller = models.CharField(max_length=10)
    date = models.DateTimeField()
    describe = models.CharField(max_length=50)


class Bids(models.Model):
    # price = models.FloatField()
    # user = models.ForeignKey()
    # item =
    pass


class Comments(models.Model):
    pass
