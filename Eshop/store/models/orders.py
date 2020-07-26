from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.CharField(max_length=500, default='1')
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    status = models.BooleanField(default=False)
    date = models.DateField(default=datetime.datetime.today)
   # image =  models.ImageField(upload_to='uploads/products/')
    def palceOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')