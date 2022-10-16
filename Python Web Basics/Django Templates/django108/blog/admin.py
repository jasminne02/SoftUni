from django.contrib import admin

from django108.blog import models


@admin.register(models.BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
