from django.db import models
from accounts.models import AbstractBaseModel, Vendor

# Create your models here.

class Product(AbstractBaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return self.name