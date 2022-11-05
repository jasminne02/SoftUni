from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from UserAndPasswordManagement.web import models
from UserAndPasswordManagement.web.models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        exclude = ('user',)

