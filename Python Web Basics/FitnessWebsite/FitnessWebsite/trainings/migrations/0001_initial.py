# Generated by Django 4.1.2 on 2022-10-22 19:48

import FitnessWebsite.trainers.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('duration', models.IntegerField()),
                ('photo', models.ImageField(upload_to='', validators=[FitnessWebsite.trainers.validators.validate_file_size])),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('start_date', models.DateField(auto_now_add=True)),
                ('trainer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.trainer')),
                ('training_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.trainingtype')),
            ],
        ),
    ]
