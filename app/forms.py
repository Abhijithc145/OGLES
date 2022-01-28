import numbers
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