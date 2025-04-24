from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.



@admin.register(Order)
class MyModelAdmin(admin.ModelAdmin):
    pass



@admin.register(OrderItem)
class MyModelAdmin(admin.ModelAdmin):
    pass