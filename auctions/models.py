from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

class Item(models.Model):
    itemName = models.CharField(max_length=64)
    price= models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=64, null=True)
    image = models.ImageField(upload_to='static/auctions/images/', null=True)

    def __str__(self):
        return f"{self.id}, {self.itemName}, {self.price}, {self.description}, {self.category}"

class AuctionListing(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name="item")
    listedBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listed_by")
    createDate = models.DateField(default=datetime.now, blank=True)
    createTime = models.TimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.item}, {self.listedBy}, {self.createDate}, {self.createTime}"

class Bidding(models.Model):
    listingInfo = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="listing_info",null=True)
    bidPrice = models.PositiveIntegerField(null=True)
    bidCount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Listing Info: {self.listingInfo}, Bid Price: {self.bidPrice}, No of Bid: {self.bidCount}"


class Comment(models.Model):
    items = models.ManyToManyField(Item, blank=True, related_name="comment_item")
    comment = models.TextField(null=True)
    userComment = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment", null=True)

    def __str__(self):
        return f"{self.items}, {self.comment}, {self.userComment}"