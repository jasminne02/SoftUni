# Generated by Django 4.1.2 on 2022-10-23 10:09

import FitnessWebsite.trainers.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0002_remove_trainingtype_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='photo',
            field=models.ImageField(default=None, upload_to='', validators=[FitnessWebsite.trainers.validators.validate_file_size]),
        ),
    ]