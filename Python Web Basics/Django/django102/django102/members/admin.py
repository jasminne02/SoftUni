from django.contrib import admin
from django102.members.models import Members


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname')
