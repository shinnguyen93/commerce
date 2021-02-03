from django.contrib import admin
from .models import AuctionListing, Bidding, Comment, User, UserProfile, Item
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    fields = ('first', 'last', 'email', 'role')

class ItemAdmin(admin.ModelAdmin):
    fields = ('itemName', 'price', 'description', 'category','image')

class AuctionListingAdmin(admin.ModelAdmin):
    fields = ('itemName', 'price', 'listedBy', 'createDate')

class BiddingAdmin(admin.ModelAdmin):
    fields = ('itemName', 'bidPrice', 'listedBy', 'category')


class CommentAdmin(admin.ModelAdmin):
    list_display = ("itemName", "comment", "username")


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Bidding, BiddingAdmin)
admin.site.register(Comment, CommentAdmin)