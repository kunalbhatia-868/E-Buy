from django.db import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from product.models import Product
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
        data['wishlisted_products']=self.request.user.wishlist_products.all()
        return data


class ProductDetailView(DetailView):
    model=Product
    context_object_name='product'
    template_name="product/product_detail.html"
    
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        return data


def addToWishlist(request,pk):
    product=get_object_or_404(Product,id=pk)
    product.wishlist_users.add(request.user)
    return HttpResponseRedirect(reverse('home'))


class WishlistListView(ListView):
    model=Product
    template_name='product/wishlist.html'
    context_object_name='wishlist_products'

    def get_queryset(self):
        return self.request.user.wishlist_products.all()

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)    