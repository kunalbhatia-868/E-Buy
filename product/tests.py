from django.test import TestCase
from .models import Product
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

        