from dataclasses import field
from .models import *

from django import forms




class prodectdetai(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)
    image1 = forms.ImageField(widget=forms.FileInput)
    image2= forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = product
        fields=['name', 'brand', 'category', 'price', 'stock', 'image', 'image1', 'image2']

# def __init__(self,*args,)        
class categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields=['name']


class brandform(forms.ModelForm):
    class Meta:
        model = Brand
        fields='__all__'        
        
class adslist(forms.ModelForm):
    class Meta:
        model = ads
        fields='__all__'   




       


    #   name = models.CharField(max_length=100)
    # discription = models.CharField(max_length=100)
    # brand =  models.ForeignKey('Brand',on_delete=models.CASCADE,null=True)
    # category =  models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    # price = models.PositiveIntegerField()
    # stock = models.PositiveIntegerField()
    # product_offer = models.PositiveIntegerField(default=0,null=True,blank=True)
    # image = models.ImageField(blank=False,upload_to="media/")
    # image1 = models.ImageField(blank=False,upload_to="media/")
    # image2 = models.ImageField(blank=False,upload_to="media/")
