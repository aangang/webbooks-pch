from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=64)
    pwd = models.CharField(max_length=64)
    tel = models.CharField(max_length=32)
