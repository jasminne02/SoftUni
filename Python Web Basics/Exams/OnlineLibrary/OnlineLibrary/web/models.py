from django.db import models


class Profile(models.Model):
    MAX_NAME_LEN = 30

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )


class Book(models.Model):
    MAX_TITLE_LEN = 30
    MAX_TYPE_LEN = 30

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
    )

    description = models.TextField()

    image = models.URLField()

    type = models.CharField(
        max_length=MAX_TYPE_LEN,
    )
