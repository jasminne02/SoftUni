from django.db import models

from FitnessWebsite.trainers import validators
from FitnessWebsite.trainers.models import Trainer


class TrainingType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class Training(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.FloatField()
    start_date = models.DateField(auto_now_add=True)
    training_type_id = models.ForeignKey(TrainingType, on_delete=models.CASCADE)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to="media", validators=(validators.validate_file_size,), default=None)

    def __str__(self):
        return self.name
