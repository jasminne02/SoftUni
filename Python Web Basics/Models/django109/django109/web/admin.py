from django.contrib import admin

from django109.web.models import Employee, Department


# This 'Employee' model is enabled in django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
