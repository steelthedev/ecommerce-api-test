from django.db import models
from accounts.models import Profile
digital = "DIGITAL"
physical = "PHYSICAL"

PRODUCT_TYPE = [
    ('Digital',digital),
    ('Physical', physical)
]


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE, default=digital)
    created_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
