from rest_framework.permissions import BasePermission
class IsStaffPermission(BasePermission):
    """
    Custom permission to only allow staff users to access certain views.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)