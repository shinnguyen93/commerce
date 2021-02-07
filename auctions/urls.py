from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listings/<int:item_id>", views.listings, name="listings"),
    path("categories",views.categories,name="categories"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("createListings",views.createListings,name="createListings"),
    path("bid",views.bid,name="bid"),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)