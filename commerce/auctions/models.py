from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    item_name = models.CharField(max_length=20)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller_item")
    date = models.DateTimeField()
    describe = models.CharField(max_length=50)


class Bid(models.Model):
    price = models.FloatField()
    user_bids = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_user")
    item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bid_item")


class Comment(models.Model):
    body = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cmt_user")
    item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="cmt_item")
