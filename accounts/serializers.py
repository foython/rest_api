from rest_framework import serializers
from .models import Vendor
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    vendor_name = serializers.CharField(required=False)
    vendor_mobile = serializers.CharField(required=False)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'role', 'vendor_name', 'vendor_mobile')
        read_only_fields = ('id',) 
        
        
    def create(self, validated_data):
            role = validated_data.get('role', 'customer').lower()
            vendor_name = validated_data.pop('vendor_name', None)
            vendor_mobile = validated_data.pop('vendor_mobile', None)

            # Validate required fields for vendors
            if role == 'vendor':
                if not vendor_name or not vendor_mobile:
                    raise serializers.ValidationError({
                        'vendor': "Vendor name and mobile must be provided for vendor accounts."
                    })

            user = User.objects.create_user(**validated_data)

            if role == 'vendor':
                Vendor.objects.create(user=user, name=vendor_name, mobile=vendor_mobile)

            return user