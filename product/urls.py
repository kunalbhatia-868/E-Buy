from django.urls import path
from .views import (
    ProductDetailView,
    HomeView,
    WishlistListView,
    addToCart,
    addToWishlist,
    WishlistListView,
    CartListView,
    CategoriesListView,
    CategoryProductListView,
    OrderCreateView
);

urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('products/wishlist/',WishlistListView.as_view(),name="wishlist"),
    path('products/<uuid:pk>/add-to-cart/',addToCart,name="add_to_cart"),
    path('products/cart/',CartListView.as_view(),name='cart'),
    path('products/categories/',CategoriesListView.as_view(),name="categories"),
    path('products/categories/<slug:slug>/',CategoryProductListView.as_view(),name="category_products"),
    path('products/order',OrderCreateView.as_view(),name="create_order"),
    path('products/<slug:slug>/',ProductDetailView.as_view(),name="detail"),
    path('products/<uuid:pk>/wishlist/',addToWishlist,name="add_to_wishlist"),
]