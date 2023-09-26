from django import forms 
from .models import Vendor , Product ,ExtendedData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CreateVendorForm (forms.ModelForm):
    class Meta: 
        model=Vendor
        fields="__all__"

class CreateProductsForm (forms.ModelForm):
    class Meta: 
        model=Product
        fields="__all__"

class AuthenticationUserForm(AuthenticationForm):
    class Meta:
        model=User
        fields = ['username','password']

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=ExtendedData
        fields ="__all__"