from django.contrib import admin
from .models import (
    Product,
    Order
)
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','status']
    list_filter=['status']
    search_fields=['title']
    class Meta:
        model=Product

class OrderAdmin(admin.ModelAdmin):
    list_display=['user','product']
    search_fields=['user','product']
    class Meta:
        model=Order


admin.site.register(Order,OrderAdmin)
admin.site.register(Product,ProductAdmin)