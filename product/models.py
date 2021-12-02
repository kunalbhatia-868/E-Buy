from django.db import models
import uuid

from django.db.models.base import Model
from users.models import UserProfile
# Create your models here.
class Product(models.Model):
    
    class StatusChoices(models.TextChoices):
        AVAILABLE="SA","Stock Available"
        OUTOFSTOCK="NSA","No Stock Available"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=256)
    slug=models.SlugField(blank=True,null=True)
    description=models.TextField()
    image=models.ImageField(blank=True,null=True)
    status=models.CharField(max_length=3,choices=StatusChoices.choices,default=StatusChoices.AVAILABLE)
    published_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]

class Order(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.product.title                