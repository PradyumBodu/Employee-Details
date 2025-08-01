from django.contrib import admin
from .models import Employees

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','desig')

admin.site.register(Employees,EmployeeAdmin)