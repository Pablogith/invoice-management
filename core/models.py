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
    street_address = models.CharField(
        max_length=100,
        default='',
        null=False)
    city = models.CharField(
        max_length=50,
        default='',
        null=False)
    country = models.CharField(
        max_length=50,
        default='',
        null=False)
    postal_code = models.CharField(
        max_length=20,
        default='',
        null=False)
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


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=50)
    net_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    gross_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])


class Invoice(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='seller_invoices')
    purchaser = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchaser_invoices')
    products = models.ManyToManyField(Product)
    invoice_number = models.CharField(max_length=50)
    sale_date = models.DateField()
    date_of_issue = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.invoice_number}"

    def get_absolute_url(self):
        return reverse('invoice-detail', args=[str(self.id)])

