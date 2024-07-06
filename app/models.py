from django.db import models

# Create your models here.

class Header(models.Model):
    logo = models.ImageField(upload_to="logo")
    phone_number = models.CharField(max_length=13)
    telegram_link = models.CharField(max_length=55)

    def __str__(self) :
       return self.phone_number

class Navbar(models.Model):
    background_image= models.ImageField(upload_to="image_bb")
    name = models.CharField(max_length=25)

    
    def __str__(self) :
       return self.name

class Tariflar(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    comapny  = models.CharField(max_length=255)
    duration = models.IntegerField()
    eating = models.IntegerField()
    viza = models.BooleanField()
    medical = models.CharField(max_length=255)
    tajriba  = models.CharField(max_length=255)
    suv = models.IntegerField()

    def __str__(self):
      return  self.name