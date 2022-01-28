from dataclasses import field
from .models import *

from django import forms




class prodectdetai(forms.ModelForm):
    class Meta:
        model = product
        fields='__all__'

# def __init__(self,*args,)        
class categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields='__all__'
        
class adslist(forms.ModelForm):
    class Meta:
        model = ads
        fields='__all__'        