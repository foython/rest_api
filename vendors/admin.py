from django.contrib import admin
from .models import Vendor
# Register your models here.
@admin.register(Vendor)
class MyModelAdmin(admin.ModelAdmin):
    pass