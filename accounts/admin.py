from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .froms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'is_staff', 'is_superuser', 'role']
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
         # Include additional fields
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password')}
            ),
    )
    ordering = ('username',)

