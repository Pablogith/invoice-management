from django import forms
from .models import Product, Invoice, User

class InvoiceForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Invoice
        fields = [
            'seller',
            'purchaser',
            'products',
            'invoice_number',
            'sale_date',
            'date_of_issue',
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'gross_price',
            'amount',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'street_address',
            'city',
            'country',
            'postal_code',
            'contact_information',
            'account_status'
        ]