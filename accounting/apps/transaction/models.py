import uuid
from django.db import models


class Payment(models.Model):
    CRYPTO = "CRYPTO"
    VISA = "VISA"
    PAYPAL = "PAYPAL"

    MONTH_CHOICES = (
        (CRYPTO, "Crypto"),
        (VISA, "VISA"),
        (PAYPAL, "Paypal"),
    )
    type = models.CharField(max_length=20,
                            choices=MONTH_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.UUIDField()
    amount = models.FloatField()
    description = models.TextField()
    payment_type = models.OneToOneField(Payment, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
