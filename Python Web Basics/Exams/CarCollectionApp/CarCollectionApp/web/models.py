from django.db import models
from django.core import validators

from CarCollectionApp.web.validators import validate_username_min_len, validate_year_values


class Profile(models.Model):
    MAX_USERNAME_LEN = 10
    MAX_PASSWORD_LEN = 30
    MAX_NAME_LEN = 30
    MIN_AGE_VALUE = 18

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=(
            validate_username_min_len,
        ),
    )

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
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
        blank=True,
        null=True,
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )


class Car(models.Model):
    MAX_TYPE_LEN = 10
    MAX_MODEL_LEN = 20
    MIN_MODEL_LEN = 2
    MIN_PRICE_VALUE = 1

    TYPE_CHOICES = [
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    ]

    type = models.CharField(
        max_length=MAX_TYPE_LEN,
        choices=TYPE_CHOICES,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LEN,
        validators=(
            validators.MinLengthValidator(MIN_MODEL_LEN),
        )
    )

    year = models.IntegerField(
        validators=(
            validate_year_values,
        )
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(MIN_PRICE_VALUE),
        ),
    )

    class Meta:
        ordering = ('pk',)

