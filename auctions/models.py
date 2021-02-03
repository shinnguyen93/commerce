from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

class UserProfile(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.CharField(max_length=100)
    userType = models.TextChoices('admin', 'user')
    role = models.CharField(blank=True, choices=userType.choices, max_length=10)

    def __str__(self):
        return f"{self.first}, {self.last}, {self.email}"

class Item(models.Model):
    itemName = models.CharField(max_length=64)
    price= models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=64)
    image = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.itemName}, {self.price}, {self.description}, {self.category}"

class AuctionListing(models.Model):
    itemName = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="listed_item")
    price = models.OneToOneField(Item, on_delete=models.CASCADE, related_name="auction_price")
    listedBy = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="listed_by")
    createDate = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.itemName}, {self.listedBy}, {self.price}, {self.creatDate}"

class Bidding(models.Model):
    itemName = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="auction_item")
    bidPrice = models.IntegerField()
    listedBy = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="bid_listed_by")
    category = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_category")

    def __str__(self):
        return f"{self.itemName}, {self.bidPrice}"


class Comment(models.Model):
    itemName = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="item_name")
    comment = models.TextField()
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return f"{self.username},{self.itemName},{self.comment}"