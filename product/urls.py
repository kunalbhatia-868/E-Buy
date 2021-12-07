from django.urls import path
from .views import ProductDetailView,HomeView, WishlistListView,addToWishlist,WishlistListView


urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('products/wishlist/',WishlistListView.as_view(),name="wishlist"),
    path('products/<slug:slug>',ProductDetailView.as_view(),name="detail"),
    path('products/wishlist/<uuid:pk>/',addToWishlist,name="add_to_wishlist")

]