from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)


class UserRole(Enum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'


class UserAccountStatus(Enum):
    ACTIVE = 'active'
    DEACTIVATED = 'deactivated'
    SUSPENDED = 'suspended'


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None)
    contact_information = models.CharField(max_length=50)
    account_status = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in UserAccountStatus])
    role = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in UserRole])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
