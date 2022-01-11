from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    full_name = models.CharField(max_length=500, default="")
    address = models.CharField(max_length=500, default="")
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class ExtraInformation(models.Model):
    nid = models.ImageField(upload_to="nid/")
    phone_no = models.CharField(max_length=20)

class Buyer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    info = models.ForeignKey(ExtraInformation, on_delete=models.CASCADE)



class LandInformation(models.Model):
    total_area = models.CharField(max_length=120)
    minimum_price = models.CharField(max_length=120)
    maximum_price = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
    latitude = models.CharField(max_length=120)
    land_image = models.ImageField(upload_to="land/")
    is_approved = models.BooleanField(default=True)


class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=CASCADE)
    info = models.ForeignKey(ExtraInformation, on_delete=models.CASCADE)
    