from django.db import models


# Create your models here.
class User(models.Model):
    id=models.IntegerField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
