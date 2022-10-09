from django.contrib import admin

from django110.web.models import Employees, Department, Project


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'level')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
