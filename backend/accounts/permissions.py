from rest_framework.permissions import BasePermission

"""Base permission classes for user access control based on user type and role."""
class BaseRolePermission(BasePermission):
    allowed_user_types = []
    allowed_roles = []

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        # Super admin bypass
        if getattr(user, "is_super_admin", False):
            return True

        # User type check
        if self.allowed_user_types and user.user_type not in self.allowed_user_types:
            return False

        # Role check
        if self.allowed_roles and user.role not in self.allowed_roles:
            return False

        return True

"""Custom permission classes for specific user types and roles."""
class IsSales(BaseRolePermission):
    allowed_user_types = ["INTERNAL"]
    allowed_roles = ["SALES"]

class IsAdmin(BaseRolePermission):
    allowed_user_types = ["INTERNAL"]
    allowed_roles = ["ADMIN"]

class IsAccounts(BaseRolePermission):
    allowed_user_types = ["INTERNAL"]
    allowed_roles = ["ACCOUNTS"]

class IsCustomer(BaseRolePermission):
    allowed_user_types = ["CUSTOMER"]


class IsStaffPermission(BasePermission):
    """
    Custom permission to only allow staff users to access certain views.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
    
# class IsSuperAdminPermission(BasePermission):
#     """
#     Custom permission to only allow super admin users to access certain views.
#     """

#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated and request.user.is_super_admin)

# class IsCustomerPermission(BasePermission):
#     """
#     Custom permission to only allow customer users to access certain views.
#     """

#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated and request.user.user_type == "CUSTOMER")
    
# class IsInternalPermission(BasePermission):
#     """
#     Custom permission to only allow internal users to access certain views.
#     """

#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated and request.user.user_type == "INTERNAL")
# class IsSalesRolePermission(BasePermission):
#     """
#     Custom permission to only allow users with Sales role to access certain views.
#     """

#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated and request.user.role == "SALES")