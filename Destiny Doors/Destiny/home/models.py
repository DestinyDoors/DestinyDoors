from unittest.util import _MAX_LENGTH
from django import forms
from django.db import models


# Create your models here.
class newboarn(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, blank=True)
    age = models.CharField(max_length=15)
    Hobby =  models.TextField(max_length=200, blank=True)
    description =  models.TextField(max_length=800, blank=True)

    def __str__(self):
        return self.child_name

class age_3_5y(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, blank=True)
    age = models.CharField(max_length=15)
    Hobby =  models.TextField(max_length=200, blank=True)
    description =  models.TextField(max_length=800, blank=True)

    def __str__(self):
        return self.child_name

class age_6_10y(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, blank=True)
    age = models.CharField(max_length=15)
    Hobby =  models.TextField(max_length=200, blank=True)
    description =  models.TextField(max_length=800, blank=True)

    def __str__(self):
        return self.child_name

class age_11_15y(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, blank=True)
    age = models.CharField(max_length=15)
    Hobby =  models.TextField(max_length=200, blank=True)
    description =  models.TextField(max_length=800, blank=True)

    def __str__(self):
        return self.child_name

class age_16_18y(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, blank=True)
    age = models.CharField(max_length=15)
    Hobby =  models.TextField(max_length=200, blank=True)
    description =  models.TextField(max_length=800, blank=True)

    def __str__(self):
        return self.child_name

'''class contactme(models.Model):
    id = models.AutoField
    First_name = models.CharField(max_length=150)
    Last_name = models.CharField(max_length=150)
    Email_Id = models.EmailField(max_length=254)
    Phone = models.IntegerField()
    Message = models.CharField(max_length=500)

    def __str__(self):
        return self.First_name
'''
    

class donateanything(models.Model):
    id = models.AutoField
    Name = models.CharField(max_length=150)
    Email_Id = models.EmailField(max_length=254)
    Phone = models.IntegerField()
    State = models.CharField(max_length=50)
    Pin = models.IntegerField()
    City = models.CharField(max_length=50)
    Donatebox = models.CharField(max_length=500)
    def __str__(self):
        return self.Name

class moneydonate(models.Model):
    id = models.AutoField
    Name = models.CharField(max_length=150)
    Email_Id = models.EmailField(max_length=254)
    Phone = models.IntegerField()
    Amount = models.IntegerField()


    def __str__(self):
        return self.Name

class winterdonation(models.Model):
    id = models.AutoField
    Name = models.CharField(max_length=150)
    Email_Id = models.EmailField(max_length=254)
    Phone = models.IntegerField()
    State = models.CharField(max_length=50)
    Pin = models.IntegerField()
    City = models.CharField(max_length=50)
    Donatebox = models.CharField(max_length=500)
    def __str__(self):
        return self.Name


class sign_up(models.Model):
    id = models.AutoField
    Name = models.CharField(max_length=150)
    Email_Id = models.EmailField(max_length=254)
    Password = models.IntegerField()
    Cpassword = models.IntegerField()
    def __str__(self):
        return self.Name


class summerdonation(models.Model):
    id = models.AutoField
    Name = models.CharField(max_length=150)
    Email_Id = models.EmailField(max_length=254)
    Phone = models.IntegerField()
    State = models.CharField(max_length=50)
    Pin = models.IntegerField()
    City = models.CharField(max_length=50)
    Donatebox = models.CharField(max_length=500)
    def __str__(self):
        return self.Name