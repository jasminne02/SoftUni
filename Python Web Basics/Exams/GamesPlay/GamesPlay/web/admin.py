from django.contrib import admin

from GamesPlay.web.models import Profile, Game


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title']
