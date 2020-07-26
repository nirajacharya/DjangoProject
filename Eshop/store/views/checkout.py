from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer


class Checkout(View):
    def post(self, request):
        # print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        print(address, phone, customer)
        cart = request.session.get('cart')
        products_on_cart = list(cart.keys())
        products = Product.get_cart_product(products_on_cart)
        print(cart,products)
        for product in products:
            product = product
            price = product.price
            quantity = cart.get(str(product.id))
            print(customer)
            order = Order(customer=Customer(id=customer), product=product, price=price, quantity=quantity, address=address,
                          phone=phone)
            order.palceOrder()
            #empty card after saving or palcing the order
            request.session['cart']={}
            # order.save() can be used as it is used in placeorder() method.
        return redirect('cartpage')
