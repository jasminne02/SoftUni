from django.db import models

from FitnessWebsite.trainings.models import Training


class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    join_date = models.DateField(auto_now_add=True)
    training_id = models.ManyToManyField(Training)
