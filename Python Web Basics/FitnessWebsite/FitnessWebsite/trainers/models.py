from django.db import models

from FitnessWebsite.trainers import validators


class Trainer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    info = models.TextField()
    photo = models.ImageField(upload_to="media", validators=(validators.validate_file_size,))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
