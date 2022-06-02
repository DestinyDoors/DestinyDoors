from django.db import models


# Create your models here.


class agegroup(models.Model):
    child_name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='upload_pic/images', default="")
    description = models.TextField(max_length=500, null=False , blank=False)

    def __str__(self):
        return self.child_name