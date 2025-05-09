from rest_framework import serializers
from .models import Product
from vendors.models import Vendor
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Product       
        fields = '__all__'
        read_only_fields = ('vendor',)        

   # fields = ['id', 'name', 'description', 'image', 'price']
   
    def create(self, validated_data):
        user = self.context['request'].user

        if user.role == 'VENDOR':
            try:
                vendor = user.vendor
            except Vendor.DoesNotExist:
                raise serializers.ValidationError("Vendor profile not found for this user.")
            
            validated_data['vendor'] = vendor
            return super().create(validated_data)

        raise serializers.ValidationError("Only vendors can create products.")

        
        
    # def update(self, instance, validated_data):
        