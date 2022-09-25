from django.db import models


class People(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=40)
