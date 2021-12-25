from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from users.models import UserProfile
from django.utils.text import slugify
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
    wishlist_users=models.ManyToManyField(UserProfile,related_name="wishlist_products",blank=True)
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)

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

    def get_total(self):
        return self.product.price * self.quantity              

class Order(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    products=models.ManyToManyField(ProductOrder)
    ordered_date=models.DateTimeField(auto_now_add=True)
    delivered=models.BooleanField(default=False)
    address=models.ForeignKey('Address',on_delete=models.SET_NULL,blank=True,null=True)


    def __str__(self):
        return self.user.username 
        
class Category(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(null=True,blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural='Categories'

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.title
     

class Address(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    apartment_number=models.CharField(max_length=200)
    street_address=models.CharField(max_length=300)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    pincode=models.IntegerField()    

    class Meta:
        verbose_name_plural='Addresses' 
