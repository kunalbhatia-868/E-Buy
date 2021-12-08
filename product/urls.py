from django.urls import path
from .views import (
    ProductDetailView,
    HomeView,
    WishlistListView,
    addToCart,
    addToWishlist,
    WishlistListView,
    CartListView
);

urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('products/wishlist/',WishlistListView.as_view(),name="wishlist"),
    path('products/<uuid:pk>/add-to-cart/',addToCart,name="add_to_cart"),
    path('products/cart/',CartListView.as_view(),name='cart'),
    path('products/<slug:slug>/',ProductDetailView.as_view(),name="detail"),
    path('products/<uuid:pk>/wishlist/',addToWishlist,name="add_to_wishlist"),


]