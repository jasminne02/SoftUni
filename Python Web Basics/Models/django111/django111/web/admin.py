from django.contrib import admin

from django111.web.models import Employees


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    pass
