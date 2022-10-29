from django.core import validators
from django.db import models


class Profile(models.Model):
    MIN_AGE_VALUE = 12
    MAX_PASSWORD_LEN = 30
    MAX_NAME_LEN = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE_VALUE),
        ),
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LEN,
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Game(models.Model):
    MAX_TITLE_LEN = 30
    MAX_CATEGORY_LEN = 15
    MIN_MAX_LEVEL_VALUE = 1
    MIN_RATING_VALUE = 0.1
    MAX_RATING_VALUE = 5

    CATEGORIES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other')
    ]

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
        unique=True,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LEN,
        choices=CATEGORIES,
    )

    rating = models.FloatField(
        validators=(
            validators.MinValueValidator(MIN_RATING_VALUE),
            validators.MaxValueValidator(MAX_RATING_VALUE),
        )
    )

    max_level = models.IntegerField(
        blank=True,
        null=True,
        validators=(
            validators.MinValueValidator(MIN_MAX_LEVEL_VALUE),
        ),
        verbose_name='Max Level'
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    summary = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('pk',)
