from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index),
    path('login/',signIn),
    path('register/',register),
    path('shop/',shop),
    path('product/<int:id>',productDetails),
    path('logout/',user_logout),
    path('cart/',cart),
    path('order/',orders),
    path('add-to-cart/<int:product_id>',addToCart),
    path('remove-from-cart/<int:cart_id>/', removeFromCart),
    path('checkout/',checkout),
    path('add-to-wishlist/<int:product_id>',add_to_wishlist),
    path('wishlist/',wishlist),
    path('remove-from-wishlist/<int:wishlist_id>',removeFromWishlist),
]