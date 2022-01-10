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
    OrderCreateView,OrderListView,
    increaseQuantityProduct,
    decreaseQuantityProduct);

urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('products/wishlist/',WishlistListView.as_view(),name="wishlist"),
    path('products/product/<uuid:pk>/add-to-cart/',addToCart,name="add_to_cart"),
    path('products/cart/',CartListView.as_view(),name='cart'),
    path('products/cart/product/<int:pk>/increase',increaseQuantityProduct,name='increase_quantity'),
    path('products/cart/product/<int:pk>/decrease',decreaseQuantityProduct,name='decrease_quantity'),
    path('products/categories/',CategoriesListView.as_view(),name="categories"),
    path('products/categories/<slug:slug>/',CategoryProductListView.as_view(),name="category_products"),
    path('products/orders/',OrderListView.as_view(),name="orders"),
    path('products/order/',OrderCreateView.as_view(),name="create_order"),
    path('products/<slug:slug>/',ProductDetailView.as_view(),name="detail"),
    path('products/product/<uuid:pk>/wishlist/',addToWishlist,name="add_to_wishlist"),
]