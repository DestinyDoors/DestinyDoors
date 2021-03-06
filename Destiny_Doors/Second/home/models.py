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


class givemoney(models.Model):
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

class partnerreg(models.Model):
    Organization = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Phone = models.IntegerField()
    Purpose = models.CharField(max_length=100)
    Date = models.DateField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.Organization

class adoptform(models.Model):
    Applicant_Name = models.CharField(max_length=80)
    Date_of_Birth = models.DateField(auto_now=False, auto_now_add=False)
    Gender = {
        ('Male','male'),
        ('Female','female')
    }
    Gender=models.CharField(max_length=10,choices=Gender)

    Category = {
        ('Indian','indian'),
        ('Nri','nri')
    }
    Category=models.CharField(max_length=10,choices=Category)

    Document = {
        ('Aadhar','aadhar'),
        ('PAN','pan'),
        ('voter','voter'),
        ('Passport','passport')

    }
    Document=models.CharField(max_length=10,choices=Document)
    ID_NO = models.CharField(max_length=80)
    Email_ID = models.CharField(max_length=80)
    Phone = models.CharField(max_length=80)

    Martital_Status = {
        ('Single','single'),
        ('Divorcee','divorcee'),
        ('Married','married'),
        ('Widow','widow')
    }
    Martital_Status=models.CharField(max_length=10,choices=Martital_Status)

    Spouse_name = models.CharField(max_length=80)
    Spouse_DOB = models.CharField(max_length=80)


    Spouse_Gender = {
        ('Male','male'),
        ('Female','female')
    }
    Spouse_Gender=models.CharField(max_length=10,choices=Spouse_Gender)

    Spouse_Category = {
        ('Indian','indian'),
        ('Nri','nri')
    }
    Spouse_Category=models.CharField(max_length=10,choices=Spouse_Category)

    Spouse_Document = {
        ('Aadhar','aadhar'),
        ('PAN','pan'),
        ('voter','voter'),
        ('Passport','passport')

    }
    Spouse_Document=models.CharField(max_length=10,choices=Spouse_Document)
    Spouse_ID_NO = models.CharField(max_length=80)
    Spouse_Email_ID = models.CharField(max_length=80)
    Spouse_Phone = models.CharField(max_length=80)

    Biological_children = models.IntegerField()
    Adopted_children = models.IntegerField()
    
    Address = models.CharField(max_length=80)
    District = models.CharField(max_length=80)
    State = models.CharField(max_length=80)
    Pin_code = models.IntegerField()

    Current_Address = models.CharField(max_length=80)
    Current_District = models.CharField(max_length=80)
    Current_State = models.CharField(max_length=80)
    Current_Pin_code = models.IntegerField()

    
  