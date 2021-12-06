from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from product.models import Product,WishlistProduct
# Create your views here.


class HomeView(ListView):
    model=Product
    template_name="product/home.html"
    paginate_by=10
    context_object_name='product_list'
    ordering=['-published_date']

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        return data


class ProductDetailView(DetailView):
    model=Product
    context_object_name='product'
    template_name="product/product_detail.html"
    
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        return data

class WishListView(ListView):
    model=WishlistProduct
    template_name="product/wishlist.html"
    context_object_name='wishlist_products'

    def get_queryset(self):
        return WishlistProduct.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        return data
