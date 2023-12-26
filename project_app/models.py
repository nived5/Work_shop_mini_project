from django.contrib.auth import login
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Login(AbstractUser):
    is_workmanager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class customer(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=100)

class workmanager(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email =  models.EmailField(max_length=100)
    address = models.CharField(max_length=100)