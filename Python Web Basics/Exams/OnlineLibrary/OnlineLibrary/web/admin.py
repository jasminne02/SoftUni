from django.contrib import admin

from OnlineLibrary.web.models import Book, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
