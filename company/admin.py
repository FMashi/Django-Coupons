from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'website')
    search_fields = ('name', 'description', 'website')

admin.site.register(Company, CompanyAdmin)
