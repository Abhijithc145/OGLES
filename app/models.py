from email.policy import default
import numbers
from random import choice
from django.db import models
from dash.models import *
from django.contrib.auth.models import AbstractUser,BaseUserManager

from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class MyUserManager(BaseUserManager):
     def create_user(self, first_name,last_name, email, number, password1=None):
        if not email:
            raise ValueError('You must have an email')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            number = number,
            is_active = 1,
        )

        user.set_password(password1)
        user.save(using=self._db)
        self.number = number
        return user


     def create_superuser(self,email,password1=None):
      
        superuser = self.model(
            email = self.normalize_email(email),
            
            is_active =1,
            is_superuser =1,
            is_staff = 1,
          
        )
        superuser.set_password(password1)
        superuser.save(using=self._db)
        return superuser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    number = models.CharField(unique=True, max_length=15)

class cartproduct(models.Model):

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=True)
    alltotal = models.PositiveIntegerField(default=True)
    quantity = models.PositiveIntegerField(default=1)
    guest = models.CharField(max_length=300,null=True)


# class  buynow(models.Model):

    # user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    # products = models.ForeignKey(product,on_delete=models.CASCADE)
    # total = models.PositiveIntegerField(default=True)
    # quantity = models.PositiveIntegerField(default=1)    
    
class user_details(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    locality = models.CharField(max_length= 100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    state = models.CharField(max_length=100)


class Coupon(models.Model):
    coupon_id=models.CharField(unique=True, max_length=6,null=True) 
    coupon_offer = models.IntegerField(default=0) 

class order_place(models.Model):

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    products = models.ForeignKey(product,on_delete=models.CASCADE) 
    address = models.ForeignKey(user_details,on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    orderdate = models.DateTimeField(auto_now_add=True)
    status = models.CharField( max_length=100,default='Placed')
    paymentmode = models.CharField(max_length=100)
    subtotal = models.BigIntegerField(null=True)
    coupons = models.ForeignKey(Coupon,on_delete=models.SET_NULL,null=True)

class wishlist_data(models.Model):

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    guest = models.CharField(max_length=300,null=True)
    
    
class buyproduct(models.Model):

    
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=True)
    quantity = models.PositiveIntegerField(default=1) 
    value = models.PositiveIntegerField(default=0)    







    

