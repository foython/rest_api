from rest_framework import serializers
from .models import Vendor
from django.contrib.auth import get_user_model

User = get_user_model()

class VendorSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Vendor
        fields = '__all__'
        

   