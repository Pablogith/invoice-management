from django import forms
from .models import User


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'address',
            'contact_information',
            'account_status',
        ]
        widgets = {
            'address': forms.Select(attrs={'class': 'form-control'}),
            'account_status': forms.Select(attrs={'class': 'form-control'}),
        }
