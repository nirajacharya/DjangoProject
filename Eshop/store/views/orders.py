from django.shortcuts import render, redirect
from django.views import View
from store.models.orders import Order
from store.middleware.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):

    #@method_decorator(auth_middleware)
    #we can use middle ware directly in our urls.py also.
    def get(self, request):
        customer_id = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer_id)
        print(orders)
        contxet={
            'orders':orders
        }
        return render(request, 'order.html',contxet)
