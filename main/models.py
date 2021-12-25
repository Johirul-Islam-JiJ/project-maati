from django.db import models
from django.db.models.fields import EmailField

# Create your models here.


class buyer(models.Model):
    name = models.CharField(max_length=200,null=False)
    phone = models.CharField(max_length=15,null=False)
    email = models.EmailField(null=True)
    nid = models.CharField(max_length=30,null = False)
    address = models.CharField(max_length=400,null=True)

    def __str__(self):
        return self.name


class seller(models.Model):
    name = models.CharField(max_length=200,null = False)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(null=False)
    nid = models.CharField(max_length=30,null=False)
    address = models.CharField(max_length=400,null=False)

    def __str__(self):
        return self.name
    
