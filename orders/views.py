from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'CUSTOMER':
            return Order.objects.filter(customer=user).prefetch_related('order_items__product')
        elif user.role == 'VENDOR':
            return Order.objects.filter(order_items__product__vendor=user.vendor).distinct().prefetch_related('order_items__product')
        else:  # ADMIN
            return Order.objects.all().select_related('customer').prefetch_related('order_items__product')

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
