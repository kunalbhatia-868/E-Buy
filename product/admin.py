from django.contrib import admin
from django.db import models
from .models import (
    Address,
    Product,
    ProductOrder,
    Order,
    Category,
    Rating
)
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','category','status']
    list_filter=['status']
    search_fields=['title']
    class Meta:
        model=Product

class ProductOrderInline(admin.TabularInline):
    model=ProductOrder

class ProductOrderAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity','ordered']
    search_fields=['user','product']
    class Meta:
        model=ProductOrder

class OrderInline(admin.TabularInline):
    model=Order


class OrderAdmin(admin.ModelAdmin):
    list_display=['user','ordering_date']
    search_fields=['user']


class AddressAdmin(admin.ModelAdmin):
    list_display=['user','pincode','state','country']
    class Meta:
        model=Address


class ProductInline(admin.TabularInline):
    model=Product
    fields=['title','status','price']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    inlines=[ProductInline]
    class Meta:
        model=Category   

class RatingAdmin(admin.ModelAdmin):
    list_display=['product','user','stars']
    search_fields=['user','product']
    
    class Meta:
        model=Rating


admin.site.register(ProductOrder,ProductOrderAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Rating,RatingAdmin)