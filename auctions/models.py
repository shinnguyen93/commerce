from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    itemName = models.CharField(max_length=64)
    price= models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=64, null=True)
    image = models.ImageField(null=True)
    listedBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listed_by")
    createDate = models.DateField(default=datetime.now, blank=True)
    createTime = models.TimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"Listing Item: {self.itemName}, Price: {self.price}"

class Bidding(models.Model):
    bidItem = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bid_item",null=True)
    bidPrice = models.PositiveIntegerField(null=True)
    bidCount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Listing Info: {self.bidItem}, Bid Price: {self.bidPrice}, No of Bid: {self.bidCount}"


class Comment(models.Model):
    commentItem = models.ManyToManyField(AuctionListing, blank=True, related_name="comment_item")
    comment = models.TextField(null=True)
    userComment = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment", null=True)

    def __str__(self):
        return f"{self.commentItem}, {self.userComment}"