from django.shortcuts import render
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):
        # print('products in cart are',list(request.session.get('cart').keys()))
        id_list = list(request.session.get('cart').keys())
        cart_products = Product.get_cart_product(id_list)
        context = {
            'products':cart_products
        }
        return render(request, 'cart.html', context)
