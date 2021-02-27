from django import forms
from .models import Admin,Custmor

class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields="__all__"

class Customer(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
