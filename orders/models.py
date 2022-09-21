from django.db import models
from products.models import Product

   
class Order(models.Model):
    user = models.ForeignKey("accounts.Profile", related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
   

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.user.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id