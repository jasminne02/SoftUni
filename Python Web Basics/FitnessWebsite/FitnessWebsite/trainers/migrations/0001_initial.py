# Generated by Django 4.1.2 on 2022-10-22 19:48

import FitnessWebsite.trainers.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('info', models.TextField()),
                ('photo', models.ImageField(upload_to='', validators=[FitnessWebsite.trainers.validators.validate_file_size])),
            ],
        ),
    ]
