from django.db import models


# Maps to a database table
class Task(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
    )

    description = models.TextField()

    priority = models.IntegerField()
