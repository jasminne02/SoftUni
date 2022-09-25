from django.contrib import admin
from django104.django_app import models


@admin.register(models.People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'age', 'country']
