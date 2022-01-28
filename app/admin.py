from django.contrib import admin
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
admin.site.register(CustomUser)
admin.site.register(cartproduct)