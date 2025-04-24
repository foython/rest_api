from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import AbstractBaseModel, CustomUser


# Create your models here.

User = get_user_model()

class Vendor(AbstractBaseModel):    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor')
    business_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    
    def __str__(self):
        return self.business_name