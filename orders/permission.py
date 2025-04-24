from rest_framework import permissions

class OrderPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.role == 'CUSTOMER'
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'ADMIN':
            return True
        if request.user.role == 'CUSTOMER':
            return obj.customer == request.user
        if request.user.role == 'VENDOR':
            return obj.order_items.filter(
                product__vendor__user=request.user
            ).exists()
        return False