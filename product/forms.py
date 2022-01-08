from django import forms
from product.models import Address, Order
from django.contrib.auth import get_user_model

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['address','payment_type']
        