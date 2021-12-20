from django.contrib import admin
from django.db import models
from .models import (
    Address,
    Product,
    ProductOrder,
    Order,
    Category
)
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','category','status']
    list_filter=['status']
    search_fields=['title']
    class Meta:
        model=Product

class ProductOrderAdmin(admin.ModelAdmin):
    list_display=['user','product','ordered']
    search_fields=['user','product']
    class Meta:
        model=ProductOrder

class OrderAdmin(admin.ModelAdmin):
    list_display=['user','ordered_date']
    search_fields=['user']



class AddressAdmin(admin.ModelAdmin):
    list_display=['user','state','country']
    class Meta:
        model=Address

class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    class Meta:
        model=Category   


admin.site.register(ProductOrder,ProductOrderAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Category,CategoryAdmin)