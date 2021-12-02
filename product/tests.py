from django.test import TestCase
from .models import Product,Order
from users.models import UserProfile

from django.utils.timezone import now
# Create your tests here.
class ProductModelTestCase(TestCase):
    def setUp(self):
        prod_1=Product.objects.create(title="New Product",description="First One")
        prod_2=Product.objects.create(title="Another New Product",description="Second One")

    def test_ProductCreateCount(self):
        qs=Product.objects.all()
        self.assertEqual(qs.count(),2)

    def test_productCheckTitle(self):
        qs=Product.objects.get(id=1)
        self.assertEqual(qs.title,"New Product")


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.prod_1=Product.objects.create(title="New Product",description="First One")
        self.prod_2=Product.objects.create(title="Another New Product",description="Second One")
        self.user_1=UserProfile.objects.create(email="test@gmail.com",password="test@121")
        self.order_1=Order.objects.create(user=self.user_1,product=self.prod_1)
        self.order_2=Order.objects.create(user=self.user_1,product=self.prod_2)

    def test_orderCount(self):
        qs=Order.objects.all()
        self.assertEqual(qs.count(),2)    

    def test_ordersPlaced(self):
        qs=Order.objects.all()
        user_qs=UserProfile.objects.all().first().order_set.all()        
        self.assertEqual(qs.count(),user_qs.count())

