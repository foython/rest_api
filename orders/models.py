from django.db import models
from accounts.models import AbstractBaseModel
from products.models import Product
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

STATUS = (
        ('ACTIVE', 'Active'),
        ('DELIVERED', 'Delivered'),
        ('PENDING', 'Pending'),
        ('SHIPED', 'Shipped'),        
    )

class Order(AbstractBaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)   
    status = models.CharField(max_length=10, choices=STATUS, default='ACTIVE')
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')

    def __str__(self):
         return f"Order #{self.id} - {self.customer}"

class OrderItem(AbstractBaseModel):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()   

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"