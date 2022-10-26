import re

from django.db import models
from django.core import exceptions


def validate_ingredients_sep_only_by_comma(value):
    pattern = re.compile(r"^([A-Za-z0-9 ()-./]+(,[A-Za-z0-9 ()-./]+)*)*$")
    if pattern.match(value) is None:
        raise exceptions.ValidationError('The ingredients should be separated by ", "')


class Recipe(models.Model):
    MAX_TITLE_LEN = 30
    MAX_INGREDIENTS_LEN = 250

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    description = models.TextField()

    ingredients = models.CharField(
        max_length=MAX_INGREDIENTS_LEN,
        validators=(
            validate_ingredients_sep_only_by_comma,
        )
    )

    time = models.IntegerField(
        verbose_name="Time (Minutes)"
    )

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.title
