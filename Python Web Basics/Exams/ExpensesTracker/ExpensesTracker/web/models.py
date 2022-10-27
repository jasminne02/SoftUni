from django.db import models


class Profile(models.Model):
    MAX_NAME_LEN = 15

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    budget = models.IntegerField()


class Expense(models.Model):
    MAX_TITLE_LEN = 50

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
    )

    image_url = models.URLField()

    description = models.TextField()

    price = models.FloatField()

    class Meta:
        ordering = ('pk',)
