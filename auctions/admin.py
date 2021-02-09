from django.contrib import admin
from .models import AuctionListing, Bidding, Comment, User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'description', 'category', 'createTime')

class BiddingAdmin(admin.ModelAdmin):
    fields = ('bidItem', 'bidPrice', 'bidCount')


class CommentAdmin(admin.ModelAdmin):
    filter_horizontal = ("commentItem",)


admin.site.register(User, UserAdmin)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Bidding, BiddingAdmin)
admin.site.register(Comment, CommentAdmin)