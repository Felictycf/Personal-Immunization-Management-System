from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)


class KeSuanInfo(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    age = models.IntegerField(default=2)
    number = models.CharField(max_length=64)
    jiating = models.CharField(max_length=64)
    vaccine = models.CharField(max_length=64)
    kesuan= models.CharField(max_length=64)
    jinzhu = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)

