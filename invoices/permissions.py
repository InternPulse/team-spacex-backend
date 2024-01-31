from rest_framework.permissions import BasePermission

class IsVerifiedPermission(BasePermission):
    message = "Please verify your account to makee use of this feature"
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_verified and user.is_active
