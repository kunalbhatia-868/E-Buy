from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(UserAdmin):

    list_display = ['email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    class Meta:
        model=UserProfile

admin.site.register(UserProfile,UserProfileAdmin)