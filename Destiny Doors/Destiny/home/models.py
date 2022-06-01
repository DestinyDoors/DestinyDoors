from django.db import models

import datetime
import os

# Create your models here.
def get_file_path(request,filename):
    original_filename = filename
    nowtime = datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    filename = "%s%s" % (nowtime.original_filename)
    return os.path.join('uploads/', filename)

class cateogry(models.Model):
    Name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=False)
    description = models.TextField(max_length=500, null=False , blank=False)

def __str__(self):
    return self.name
   
class agegroup(models.Model):
    cateogry = models.ForeignKey(cateogry, on_delete=models.CASCADE)
    Name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=False)
    description = models.TextField(max_length=500, null=False , blank=False)

def __str__(self):
    return self.name