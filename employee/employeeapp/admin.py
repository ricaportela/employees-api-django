from django.contrib import admin

from employeeapp.models import Departament, Employee


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('description',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'departament')
