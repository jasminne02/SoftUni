from django.core.exceptions import ValidationError
from django import forms
from django113.web import models


def validate_text(value):
    if '_' in value:
        raise ValidationError('`_` is invalid for `text`')


def validate_priority(value):
    if value < 1 or 10 > value:
        raise ValidationError('Priority must be between 1 and 10')


class ToDoForms(forms.Form):
    text = forms.CharField(
        validators=(
            validate_text,
            validate_priority,
        ),
    )
    is_done = forms.BooleanField(
        required=False,
    )


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = '__all__'
