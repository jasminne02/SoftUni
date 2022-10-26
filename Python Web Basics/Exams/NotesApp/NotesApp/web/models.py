from django.db import models


class Note(models.Model):
    MAX_TITLE_LEN = 30

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
    )

    image_url = models.URLField(
        verbose_name='Link to Image'
    )

    content = models.TextField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.title


class Profile(models.Model):
    MAX_NAME_LEN = 20

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    age = models.PositiveIntegerField()

    image_url = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
