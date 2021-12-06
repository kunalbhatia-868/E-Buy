from django.urls import path
from .views import ProductDetailView,HomeView,WishListView


urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('products/wishlist/',WishListView.as_view(),name="wishlist"),
    path('products/<slug:slug>',ProductDetailView.as_view(),name="detail")

]