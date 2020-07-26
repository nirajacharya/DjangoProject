from django.urls import path
from .views import home, login, signup, cart, checkout, orders
from store.middleware.auth import auth_middleware

urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.SignUp.as_view(), name='signuppage'),
    path('login', login.Login.as_view(), name='loginpage'),
    path('logout', login.Logout.as_view(), name='logoutpage'),
    path('cart', cart.Cart.as_view(), name='cartpage'),
    path('checkout', checkout.Checkout.as_view(), name='checkoutpage'),
    #using middleware in urls.py
    path('order', auth_middleware(orders.OrderView.as_view()), name='orderpage'),

]
