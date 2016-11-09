from django.contrib import admin

from employees.core.models import Departament, Employees


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('description',)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'departament')

