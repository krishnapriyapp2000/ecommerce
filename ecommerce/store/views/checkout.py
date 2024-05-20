from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        request.session['address'] = request.POST.get('address')
        request.session['phone'] = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        # print(address, phone, customer, cart, products)
        # for product in products:
        #     print(cart.get(str(product.id)))
        #     order = Order(customer=Customer(id=customer),
        #                   product=product,
        #                   price=product.price,
        #                   address=address,
        #                   phone=phone,
        #                   quantity=cart.get(str(product.id)))
        #     order.save()
        # request.session['cart'] = {}

        # return redirect('cart')
       
        return redirect('payment')

def payment(request):
    if request.POST:
        address = request.session.get('address')
        phone = request.session.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        paymethod = request.POST.get('pay')
        products = Products.get_products_by_id(list(cart.keys()))
        if paymethod == 'Cash on Delivary':
            for product in products:
                print(cart.get(str(product.id)))
                order = Order(customer=Customer(id=customer),
                                product=product,
                                price=product.price,
                                address=address,
                                phone=phone,
                                paymethod = paymethod,
                                quantity=cart.get(str(product.id)))
                order.save()
                request.session['cart'] = {}
        elif paymethod == 'RazorPay':
            return redirect('razorpay')
        elif paymethod == 'Paypal':
            return redirect('checkout_payment')
        elif paymethod == 'Credit Card':
            return redirect('creditcard')
        return redirect('cart')
    return render(request, 'payment.html')


   
