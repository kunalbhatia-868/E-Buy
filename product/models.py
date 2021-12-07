from django.db import models
import uuid
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _
from users.models import UserProfile
# Create your models here.
class Product(models.Model):
    
    class StatusChoices(models.TextChoices):
        AVAILABLE="SA",_("Stock Available")
        OUTOFSTOCK="NSA",_("No Stock Available")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=256)
    slug=models.SlugField(blank=True,null=True)
    description=models.TextField()
    image=models.ImageField(blank=True,null=True)
    status=models.CharField(max_length=3,choices=StatusChoices.choices,default=StatusChoices.AVAILABLE)
    published_date=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(default=0)
    wishlist_users=models.ManyToManyField(UserProfile,related_name="wishlist_products")

    def __str__(self):
        return self.title[:50]

class ProductOrder(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    ordered=models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ordered Product'
        verbose_name_plural='Ordered Products' 

    def __str__(self):
        return self.product.title                

class Order(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    products=models.ManyToManyField(ProductOrder)
    ordered_date=models.DateTimeField(auto_now_add=True)
    delivered=models.BooleanField(default=False)
    address=models.ForeignKey('Address',on_delete=models.SET_NULL,blank=True,null=True)


    def __str__(self):
        return self.user.username 
     
class Address(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    apartment_number=models.CharField(max_length=200)
    street_address=models.CharField(max_length=300)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    pincode=models.IntegerField()    

    class Meta:
        verbose_name_plural='Addresses' 

# class WishlistProduct(models.Model):
#     user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.product.title        