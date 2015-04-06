from django.contrib import admin
from company.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'url', 'slug')
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Company, CompanyAdmin)
