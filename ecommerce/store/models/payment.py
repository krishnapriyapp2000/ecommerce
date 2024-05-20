from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.db import models

class Payment(models.Model):
    cc_number = CardNumberField(('card number'))
    cc_expiry = CardExpiryField(('expiration date'))
    cc_code = SecurityCodeField(('security code'))