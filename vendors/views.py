from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import VendorSerializer
from accounts.models import Vendor

User = get_user_model()

# Create your views here.
class VendorView(APIView):    
    
    def get(self, request, *args, **kwargs):
        queryset = Vendor.objects.select_related('user').all()

        if request.user.role == 'ADMIN':
            serializer = VendorSerializer(queryset, many=True)
            return Response(serializer.data)  
        else:
            vendor = queryset.filter(user=request.user).first()
            if not vendor:
                return Response({'detail': 'Vendor profile not found.'}, status=404)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data) 
    