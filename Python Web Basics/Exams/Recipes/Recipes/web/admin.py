from django.contrib import admin

from Recipes.web.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
