# Generated by Django 4.1.2 on 2022-10-08 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_department_employees_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
