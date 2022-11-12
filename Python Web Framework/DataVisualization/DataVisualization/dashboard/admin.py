from django.contrib import admin

from .models import CountryData, TownData


@admin.register(CountryData)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country', 'population')


@admin.register(TownData)
class TownAdmin(admin.ModelAdmin):
    list_display = ('town', 'population')

