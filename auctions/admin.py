from django.contrib import admin
from .models import AuctionListing, Bidding, Comment, User, Item


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    fields = ('itemName', 'price', 'description', 'category', 'image')

class AuctionListingAdmin(admin.ModelAdmin):
    fields = ('item', 'listedBy', 'createDate', 'createTime')

class BiddingAdmin(admin.ModelAdmin):
    fields = ('item', 'bidPrice','listedBy')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('item', 'comment', 'userComment')


admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Bidding, BiddingAdmin)
admin.site.register(Comment, CommentAdmin)