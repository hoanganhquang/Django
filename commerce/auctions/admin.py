from django.contrib import admin
from .models import *
# Register your models here.


class AucAdmin(admin.ModelAdmin):
    list_display = ("id", "item_name", "price", "seller", "date", "describe")


class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "price", "user_bids", "item")


admin.site.register(User)
admin.site.register(AuctionListing, AucAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment)
