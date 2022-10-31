from django.contrib import admin

from CarCollectionApp.web.models import Profile, Car


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['type', 'model']
