from django import db
from django.db import models
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from product.models import Product, ProductOrder,Category,Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
# Create your views here.


class HomeView(ListView):
    model=Product
    template_name="product/home.html"
    paginate_by=20
    context_object_name='product_list'
    ordering=['-published_date']

    def get_queryset(self):
        return super().get_queryset()

    
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
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


@login_required
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
        data=super().get_context_data(**kwargs)
        cart_total=0
        total_items=0
        for item in data['cart_products']:
            cart_total+=item.total
            total_items+=1;

        data['cart_total']=cart_total
        data['total_items']=total_items

        return data

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user)

@login_required
def addToCart(request,pk,quantity=1):
    product=get_object_or_404(Product,id=pk)
    ordered_products=ProductOrder.objects.filter(user=request.user)
    qs_inCart=ordered_products.filter(product=product)
    if qs_inCart.exists():
        qs_inCart.delete()
    else:
        ProductOrder.objects.create(user=request.user,product=product,quantity=quantity)    

    return HttpResponseRedirect(reverse('home'))

class OrderCreateView(LoginRequiredMixin,CreateView):
    form_class=OrderForm
    model=Order
    template_name="product/order_create.html"
    success_url="/"

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['ordered_products']=self.request.user.productorder_set.all()

        total_items=0;
        cart_total=0;

        for item in data['ordered_products']:
            total_items+=1
            cart_total+=item.total

        data['cart_total']=cart_total
        data['total_items']=total_items    
        return data

    def form_valid(self, form):
        form.instance.user=self.request.user
        form.save()
        
        product_order_list=ProductOrder.objects.filter(user=self.request.user).values('product')
        product_list=Product.objects.filter(id__in=product_order_list)
        form.instance.products.set(product_list)
        form.save()

        # Also delete all product orders(cart_products) of this user
        self.request.user.productorder_set.all().delete()
        return super().form_valid(form)


class OrderListView(LoginRequiredMixin,ListView):
    model=Order
    context_object_name="order_products"
    ordering=['-ordering_date']
    template_name="product/order_list.html"

    def get_queryset(self):
        qs_product_list=super().get_queryset().filter(user=self.request.user,delivered=False).values_list('products')
        data=Product.objects.filter(id__in=qs_product_list)
        return data

class CategoriesListView(ListView):
    model=Category
    context_object_name="categories"
    ordering=['title']
    template_name="product/categories_list.html"

class CategoryProductListView(ListView):
    model=Product
    context_object_name='category_products'
    template_name='product/category_product_list.html'
    ordering=['-published_date']
    paginate_by=20

    def get_queryset(self):
        return super().get_queryset().filter(category__slug=self.kwargs['slug']) 

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            i=0
            for product in data['category_products']:
                qs=product.wishlist_users.filter(id=self.request.user.id)
                if qs.exists():
                    data['category_products'][i].is_wishlisted=True
                else:
                    data['category_products'][i].is_wishlisted=False
                i+=1

            i=0
            for product in data['category_products']:
                qs=ProductOrder.objects.filter(user=self.request.user).filter(product=product)
                if qs.exists():
                    data['category_products'][i].is_in_cart=True
                else:
                    data['category_products'][i].is_in_cart=False
                i+=1
        data['category']=Category.objects.get(slug=self.kwargs['slug'])
        return data

