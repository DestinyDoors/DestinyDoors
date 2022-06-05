from django.db import models


# Create your models here.


class newboarn(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, null=False , blank=False)
    age = models.CharField(max_length=15, null=False, blank=False)
    Hobby =  models.TextField(max_length=200, null=True , blank=True)
    description =  models.TextField(max_length=800, null=False , blank=False)

    def __str__(self):
        return self.child_name

class age_3_5y(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, null=False , blank=False)
    age = models.CharField(max_length=15, null=False, blank=False)
    Hobby =  models.TextField(max_length=200, null=False , blank=False)
    description =  models.TextField(max_length=800, null=False , blank=False)

    def __str__(self):
        return self.child_name

class age_6_10y(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, null=False , blank=False)
    age = models.CharField(max_length=15, null=False, blank=False)
    Hobby =  models.TextField(max_length=200, null=False , blank=False)
    description =  models.TextField(max_length=800, null=False , blank=False)

    def __str__(self):
        return self.child_name

class age_11_15y(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, null=False , blank=False)
    age = models.CharField(max_length=15, null=False, blank=False)
    Hobby =  models.TextField(max_length=200, null=False , blank=False)
    description =  models.TextField(max_length=800, null=False , blank=False)

    def __str__(self):
        return self.child_name

class age_16_18y(models.Model):
    id = models.AutoField
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    taught = models.TextField(max_length=200, null=False , blank=False)
    age = models.CharField(max_length=15, null=False, blank=False)
    Hobby =  models.TextField(max_length=200, null=False , blank=False)
    description =  models.TextField(max_length=800, null=False , blank=False)

    def __str__(self):
        return self.child_name