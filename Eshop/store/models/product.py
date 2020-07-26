from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default='')
   # image =  models.ImageField(upload_to='uploads/products/')
    def __str__(self):
       return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    @staticmethod
    def get_cart_product(list_ids):
        #id=id for 1 id for many id we use id__in=list_ids
        return Product.objects.filter(id__in=list_ids)

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()
