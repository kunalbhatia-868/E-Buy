from django.shortcuts import render
from django.views.generic.list import ListView

from product.models import Product
# Create your views here.


class Home(ListView):
    model=Product
    template_name="product/home.html"
    paginate_by=10
    context_object_name='product_list'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        return data