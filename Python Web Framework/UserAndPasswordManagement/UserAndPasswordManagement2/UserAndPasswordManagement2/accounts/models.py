import datetime

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models


def validate_age_through_birthday(value):
    age = (datetime.date.today() - value).days / 365
    if age < 18:
        raise validators.ValidationError("You must be at least 18 years old")


class CustomUser(AbstractUser):
    birthday = models.DateField(
        validators=(
            validate_age_through_birthday,
        )
    )
    # add additional fields in here

    REQUIRED_FIELDS = ['birthday']

    def __str__(self):
        return self.username
