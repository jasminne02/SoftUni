# Generated by Django 4.1.2 on 2022-10-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('level', models.CharField(choices=[('jr.', 'Junior'), ('mid.', 'Middle'), ('sr.', 'Senior')], max_length=4)),
            ],
        ),
    ]
