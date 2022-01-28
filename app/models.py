from email.policy import default
import numbers
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
    first_name = models.EmailField(max_length=100)
    last_name = models.EmailField(max_length=100)
    email = models.EmailField(unique=True)
    number = models.CharField(unique=True, max_length=15)

class cartproduct(models.Model):

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=True)
    quantity = models.PositiveIntegerField(default=1)
    
