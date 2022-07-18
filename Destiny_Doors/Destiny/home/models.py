from faulthandler import disable
from tkinter import DISABLED
from tokenize import Name
from unicodedata import category
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

class moneydonate(models.Model):
    id = models.AutoField
    Name = models.CharField(max_length=150)
    Email_Id = models.EmailField(max_length=254)
    Phone = models.IntegerField()
    Card_no = models.CharField(max_length=50)
    Exp = models.CharField(max_length=50)
    Cvv = models.CharField(max_length=50)
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

class booking_table(models.Model):
    id = models.AutoField
    Name = models.CharField(max_length=80)
    Email = models.EmailField(max_length=80)
    Purpose = models.CharField(max_length=80)
    Date = models.CharField(max_length=90)
    def __str__(self):
        return self.Name


class parent_adopted_form(models.Model):
    Name=models.CharField(max_length=30)
    DOB=models.DateField(auto_now=False, auto_now_add=False)
    Aadhar=models.IntegerField()
    Email=models.EmailField(max_length=254)
    Phone=models.IntegerField()
    Biological_Childrens=models.IntegerField()
    Adopted_Children=models.IntegerField()

    Address=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    State=models.CharField(max_length=30)
    Pincode=models.IntegerField()
    def __str__(self):
        return self.Name