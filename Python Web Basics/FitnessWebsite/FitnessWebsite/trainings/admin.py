from django.contrib import admin

from FitnessWebsite.trainings.models import Training, TrainingType


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'start_date']


@admin.register(TrainingType)
class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration']
