from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name
        
# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    # discription = models.CharField(max_length=100)
    brand =   models.CharField(max_length=100)
    category =  models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(blank=False,upload_to="media/")
    image1 = models.ImageField(blank=False,upload_to="media/")
    image2 = models.ImageField(blank=False,upload_to="media/")


class ads(models.Model):
    homeimage = models.ImageField(blank=False,upload_to="")
    homeimage1 = models.ImageField(blank=True,upload_to="")
    menimage = models.ImageField(blank=False,upload_to="")
    menimage1 = models.ImageField(blank=True,upload_to="")
    womenimage = models.ImageField(blank=False,upload_to="")
    womenimage1 = models.ImageField(blank=True,upload_to="")
    sportsimage = models.ImageField(blank=False,upload_to="")
    sportsimage1 = models.ImageField(blank=True,upload_to="")

    
