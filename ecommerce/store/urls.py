from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut, payment
from .views.orders import OrderView
from .views.razorpay import Razorpay,paymenthandler
from .views.creditcard import CreditCard
from .views.paypal import payment_checkout, create_payment, execute_payment, payment_failed
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('payment', payment , name='payment'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('razorpay', Razorpay.as_view(), name='razorpay'),
    path('paymenthandler', paymenthandler, name='paymenthandler'),
    path('paypal_checkout', payment_checkout, name='checkout_payment'),
    path('create_payment', create_payment, name='create_payment'),
    path('execute_payment', execute_payment, name='execute_payment'),
    path('payment_failed', payment_failed, name='payment_failed'),
    path('creditcard', CreditCard, name='creditcard'),

]