from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

from .models import User, AuctionListing, Bidding, Comment


def index(request):
    return render(request, "auctions/index.html",{
        "items": AuctionListing.objects.all()
    })


def listings(request, item_id):
    try:
        item = Bidding.objects.get(id=item_id)
    except Bidding.DoesNotExist:
        raise Http404("Item does not Exist!!!!")
    return render(request, "auctions/listings.html",{
        "item":item
    })

def bid(request):
    pass

def categories(request):
    pass

def watchlist(request):
    pass

def createListings(request):
    return render(request, "auctions/createListings.html")


def create(request):
     if request.method == "POST":
        try:
            itemName = request.POST.get("itemName")
            description = request.POST.get("description")
            price = request.POST.get("price")
            category = request.POST.get("category")
            user = request.user
            image = request.FILES["image"]
            fs = FileSystemStorage()
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        newListing = AuctionListing()
        newListing.itemName=itemName
        newListing.price=price
        newListing.description=description
        newListing.category=category
        newListing.listedBy=user
        newListing.image=image
        newListing.save()
        fs.save(image.name. image)
        return HttpResponseRedirect(reverse("index"))



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
