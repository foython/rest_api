from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


#this model fields will be created whom inharite this class
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
#using django AbstractUser class and default username authentication as requirment
class CustomUser(AbstractUser):
    ROLES = (
        ('ADMIN', 'Admin'),
        ('VENDOR', 'Vendor'),
        ('CUSTOMER', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='CUSTOMER')
    
    def user_role(self):
        return self.user.role
    
    
    
    
class Vendor(AbstractBaseModel):
    name = models.CharField(max_length=128)
    mobile = models.CharField(max_length=15)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name