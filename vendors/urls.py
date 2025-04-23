from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorView



urlpatterns = [   
    path('api', VendorView.as_view(), name='vendor'),      
]
