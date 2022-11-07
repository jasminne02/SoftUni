from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', "birthday")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.__remove_help_texts()

    def save(self, commit=True):
        return super().save(commit=commit)

    def __remove_help_texts(self):
        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username",)


