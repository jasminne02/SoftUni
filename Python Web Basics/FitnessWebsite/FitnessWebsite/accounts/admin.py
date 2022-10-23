from django.contrib import admin

from FitnessWebsite.accounts.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'password', 'join_date']
