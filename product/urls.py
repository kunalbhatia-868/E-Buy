from django.urls import path
from .views import (
    ProductDetailView,
    HomeView,
    WishlistListView,
    UpdateCart,
    addToWishlist,
    WishlistListView,
    CartListView,
    CategoriesListView,
    CategoryProductListView,
    OrderCreateView,OrderListView,
    increaseQuantityProduct,
    decreaseQuantityProduct,
    removeFromCartPage,
    get_categories_list
)

urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('products/wishlist/',WishlistListView.as_view(),name="wishlist"),
    path('products/cart/',CartListView.as_view(),name='cart'),
    path('products/categories/',CategoriesListView.as_view(),name="categories"),
    path('products/categories_list/',get_categories_list,name="get_categories"),
    path('products/categories/<slug:slug>/',CategoryProductListView.as_view(),name="category_products"),
    path('products/orders/',OrderListView.as_view(),name="orders"),
    path('products/order/',OrderCreateView.as_view(),name="create_order"),
    path('products/<slug:slug>/',ProductDetailView.as_view(),name="detail"),
    
]
htmx_urlpatterns=[
    path('products/cart/product/<int:pk>/increase',increaseQuantityProduct,name='increase_quantity'),
    path('products/cart/product/<int:pk>/decrease',decreaseQuantityProduct,name='decrease_quantity'),
    path('products/product/update-cart/<uuid:pk>/',UpdateCart,name="update_cart"),
    path('products/product/wishlist/<uuid:pk>/',addToWishlist,name="add_to_wishlist"),
    path('products/product/remove-from-cart/<uuid:pk>/',removeFromCartPage,name="remove_from_cart"),
]
urlpatterns+=htmx_urlpatterns