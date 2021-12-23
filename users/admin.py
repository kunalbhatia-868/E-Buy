from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile,Seller
from product.admin import ProductOrderInline,OrderInline
# Register your models here.


class UserProfileAdmin(UserAdmin):
    list_display = ['username','email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('username','email', 'password','type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
        ('Important Dates',{'fields':('last_login','date_joined')}),
        ('Advanced Options',{'fields':('user_permissions','groups'),
            'classes':('collapse',),
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    inlines=[ProductOrderInline,OrderInline]
    class Meta:
        model=UserProfile



class SellerAdmin(admin.ModelAdmin):
    list_display = ['username','email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('username','email', 'password','type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
        ('Important Dates',{'fields':('last_login','date_joined')}),
        ('Advanced Options',{'fields':('user_permissions','groups'),
            'classes':('collapse',),
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    
    class Meta:
        model=Seller




admin.site.register(Seller,SellerAdmin)
admin.site.register(UserProfile,UserProfileAdmin)