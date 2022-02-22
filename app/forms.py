from dataclasses import field
import numbers
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name', 'email', 'number']
        

class loginform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Enter username'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))

class addressform(forms.ModelForm):
    class Meta:
        model = user_details
        fields=['locality','city','pincode','state']   


class couponform(forms.ModelForm):
    coupon_id  =  forms.CharField(label="Coupon Code", max_length=6,required=True,widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': 'Enter the Coupon Code'}))
    coupon_offer = forms.IntegerField(label='Discount in %', required=True, widget=forms.TextInput(
                                 attrs={'min': 1, 'max': '90', 'type': 'number', 'placeholder': 'Enter the Coupon Offer'}))
    class Meta:
        model = Coupon
        fields='__all__'   



class editeprofileform(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [ 'first_name','last_name', 'email', 'number']

   