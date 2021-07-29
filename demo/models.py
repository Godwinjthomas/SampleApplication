from django.db import models
from django.contrib.auth.models import User


class Login(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)


class Registration(models.Model):
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    zip = models.CharField(max_length=10)
    email = models.EmailField()

