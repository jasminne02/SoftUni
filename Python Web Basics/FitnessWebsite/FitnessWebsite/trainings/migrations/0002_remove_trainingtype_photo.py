# Generated by Django 4.1.2 on 2022-10-23 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingtype',
            name='photo',
        ),
    ]
