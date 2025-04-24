from django.db import models
from accounts.models import AbstractBaseModel
from vendors.models import Vendor

# Create your models here.

class Product(AbstractBaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    stock = models.PositiveIntegerField()
    
    
    def __str__(self):
        return self.name