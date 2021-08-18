from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from .models import *


def index(request):
    item_list = AuctionListing.objects.all()
    return render(request, "auctions/index.html", {
        "items": item_list
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_item(request):
    user = request.user
    if user.id is None:
        return redirect("login_view")

    if request.method == "POST":
        seller = user
        item_name = request.POST["item-name"]
        price = request.POST["price"]
        describe = request.POST["describe"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_item = AuctionListing.objects.create(item_name=item_name, price=price, seller=seller, date=date, describe=describe)
        new_item.save()

        return redirect('index')

    return render(request, 'auctions/create-item.html')


def item_detail(request, item_id):
    item = AuctionListing.objects.get(pk=int(item_id))
    current_user_id = request.user.id
    current_user = User.objects.get(pk=int(current_user_id))

    if request.method == "POST":
        price = request.POST["bid"]
        new_bid = Bid.objects.create(price=price, user_bids=request.user, item=item)
        new_bid.save()

    context = {
        "item": item,
        # "current_bid": current_bid
    }

    return render(request, 'auctions/item.html', context)
