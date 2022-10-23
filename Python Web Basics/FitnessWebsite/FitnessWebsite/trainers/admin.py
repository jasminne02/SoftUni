from django.contrib import admin

from FitnessWebsite.trainers.models import Trainer


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'info')
