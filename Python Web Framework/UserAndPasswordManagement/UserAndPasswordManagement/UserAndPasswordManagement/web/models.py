from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.forms import UserCreationForm

from UserAndPasswordManagement.web.managers import AppUsersManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    if_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'name'

    objects = AppUsersManager()

    class Meta:
        app_label = 'myapp'


class Profile(models.Model):
    # first name
    # last_name
    # profile image

    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)


