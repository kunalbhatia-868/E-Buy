from django.db import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from product.models import Product, ProductOrder
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(LoginRequiredMixin,ListView):
    model=Product
    template_name="product/home.html"
    paginate_by=10
    context_object_name='product_list'
    ordering=['-published_date']

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        i=0
        for product in data['product_list']:
            qs=product.wishlist_users.filter(id=self.request.user.id)
            if qs.exists():
                data['product_list'][i].is_wishlisted=True
            else:
                data['product_list'][i].is_wishlisted=False
            i+=1

        i=0
        for product in data['product_list']:
            qs=ProductOrder.objects.filter(user=self.request.user).filter(product=product)
            if qs.exists():
                data['product_list'][i].is_in_cart=True
            else:
                data['product_list'][i].is_in_cart=False
            i+=1
                  
        return data


class ProductDetailView(LoginRequiredMixin,DetailView):
    model=Product
    context_object_name='product'
    template_name="product/product_detail.html"
    
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        return data


def addToWishlist(request,pk):
    product=get_object_or_404(Product,id=pk)
    if product.wishlist_users.filter(id=request.user.id).exists():
        product.wishlist_users.remove(request.user)
    else:
        product.wishlist_users.add(request.user)
    return HttpResponseRedirect(reverse('home'))    


class WishlistListView(LoginRequiredMixin,ListView):
    model=Product
    template_name='product/wishlist.html'
    context_object_name='wishlist_products'

    def get_queryset(self):
        data=self.request.user.wishlist_products.all()
        i=0
        for product in data:
            qs=ProductOrder.objects.filter(user=self.request.user,product=product)
            if qs.exists():
                data[i].is_in_cart=True
            else:
                data[i].is_in_cart=False
            i+=1
        return data

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)    

class CartListView(LoginRequiredMixin,ListView):
    model=ProductOrder
    template_name='product/cart.html'
    context_object_name='cart_products'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user)

def addToCart(request,pk,quantity=1):
    product=get_object_or_404(Product,id=pk)
    ordered_products=ProductOrder.objects.filter(user=request.user)
    qs_inCart=ordered_products.filter(product=product)
    if qs_inCart.exists():
        qs_inCart.delete()
    else:
        ProductOrder.objects.create(user=request.user,product=product,quantity=quantity)    

    return HttpResponseRedirect(reverse('home'))