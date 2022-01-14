from django import forms
from product.models import Address, Order, ProductOrder

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['address','payment_type']
        

class CartForm(forms.ModelForm):
    class Meta:
        model=ProductOrder
        fields=['quantity']        