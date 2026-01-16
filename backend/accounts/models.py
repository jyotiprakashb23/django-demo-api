from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import uuid

def generate_user_id():
    return f"USR-{uuid.uuid4().hex[:8].upper()}"

class User(AbstractUser):
    # Enum for user types
    choices = [("CUSTOMER", "Customer"), ("INTERNAL", "Internal")]
    role = [("SALES", "Sales"), ("ADMIN", "Admin"), ("SUPPORT", "Support"), ("ACCOUNTS", "Accounts")]
    
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=50, choices=choices, default="CUSTOMER")
    role = models.CharField(max_length=50, choices=role, null=True)
    is_super_admin = models.BooleanField(default=False)
    # user_id = models.CharField(unique=True, max_length=100)
    user_id = models.CharField(
        max_length=100,
        unique=True,
        default=generate_user_id,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="created_users",
    )
    updated_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="updated_users",
    )

    def __str__(self):
        return self.username
