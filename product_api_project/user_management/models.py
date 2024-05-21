from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)