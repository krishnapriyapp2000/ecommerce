from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from django import forms

class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')

    # class Meta:
    #     model = Payment
    #     fields = ('cc_number', '')