from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class LoginForm(forms.Form):
    sername = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class productsform(forms.ModelForm):
    name =forms.CharField(max_length=50)
    class Meta:
        model = Products
        fields = ['name', 'P_img','price','description']