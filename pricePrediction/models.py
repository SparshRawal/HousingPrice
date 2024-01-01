from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import os
# Create your models here.

class HouseFeatures(models.Model):

    IntendedUse = models.CharField(max_length=255)
    Deed = models.CharField(max_length=255)
    Financing = models.CharField(max_length=255)
    BuyerSellerRelated = models.CharField(max_length=255)
    Solar = models.CharField(max_length=255)
    PersonalProperty = models.CharField(max_length=255)
    PartialInterest = models.CharField(max_length=255)
    CLASS = models.IntegerField()
    STORIES = models.IntegerField()
    ROOMS = models.IntegerField()
    QUALITY = models.IntegerField()
    HEAT = models.IntegerField()
    COOL = models.IntegerField()
    BATHFIXTUR = models.IntegerField()
    SQFT = models.IntegerField()
    GARAGE = models.IntegerField()
    LON = models.FloatField()
    LAT = models.FloatField()
    ZIP = models.IntegerField()
    