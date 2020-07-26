from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'phone', 'email']


class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'customer','address','phone','product','quantity','price']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
