from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order
from store.models.payment import Payment

from store.forms import PaymentForm

def CreditCard(request):
    if request.method == 'POST': 
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart')
    else:
        form = PaymentForm()
    return render(request, 'creditcard.html', {'form': form})