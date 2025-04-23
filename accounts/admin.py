from django.contrib import admin
from .models import CustomUser, Vendor

# Register your models here.

@admin.register(CustomUser)
class MyModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Vendor)
class MyModelAdmin(admin.ModelAdmin):
    pass