from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','status']
    list_filter=['status']
    search_field=['title']
    class Meta:
        model=Product


admin.site.register(Product,ProductAdmin)