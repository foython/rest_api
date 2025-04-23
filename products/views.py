from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

class IsVendor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'VENDOR'

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'CUSTOMER'
    

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('vendor').all() 
    serializer_class = ProductSerializer  
    
        
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        if user.role == 'VENDOR':
            return queryset.filter(vendor__user=user)
        return queryset
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsVendor()]
        return [permissions.IsAuthenticated()]