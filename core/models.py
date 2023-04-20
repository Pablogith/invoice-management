from enum import Enum
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser


class UserRole(Enum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'


class UserAccountStatus(Enum):
    ACTIVE = 'active'
    DEACTIVATED = 'deactivated'
    SUSPENDED = 'suspended'


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100, default='', null=False)
    city = models.CharField(max_length=50, default='', null=False)
    country = models.CharField(max_length=50, default='', null=False)
    postal_code = models.CharField(max_length=20, default='', null=False)
    contact_information = models.CharField(max_length=50)
    account_status = models.CharField(
        max_length=20,
        choices=[(status.value, status.value.title()) for status in UserAccountStatus],
        default=UserAccountStatus.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
