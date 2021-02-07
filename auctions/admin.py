from django.contrib import admin
from .models import AuctionListing, Bidding, Comment, User, Item


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    fields = ('itemName', 'price', 'description', 'category', 'image')

class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'listedBy', 'createDate', 'createTime')

class BiddingAdmin(admin.ModelAdmin):
    fields = ('listingInfo', 'bidPrice', 'bidCount')


class CommentAdmin(admin.ModelAdmin):
    filter_horizontal = ("items",)


admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Bidding, BiddingAdmin)
admin.site.register(Comment, CommentAdmin)