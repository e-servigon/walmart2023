from django import forms
from .models import Vendor,Product

class CreateVendorForm(forms.ModelForm):
    class Meta:
        model=Vendor
        fields="__all__"
        
class CreateProductsForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
    