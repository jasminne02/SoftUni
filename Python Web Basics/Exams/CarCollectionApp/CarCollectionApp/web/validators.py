from django.core import validators


def validate_username_min_len(value):
    if len(value) < 2:
        raise validators.ValidationError("The username must be a minimum of 2 chars")


def validate_year_values(value):
    if value < 1980 or value > 2049:
        raise validators.ValidationError("Year must be between 1980 and 2049")
