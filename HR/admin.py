from django.contrib import admin
from HR.models import Job, Employee


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_jobs')

admin.site.register(Job, JobAdmin)
admin.site.register(Employee, EmployeeAdmin)
