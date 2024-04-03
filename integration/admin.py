from django.contrib import admin
from .models import IntegrationService

class IntegrationServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'last_synced_at')
    search_fields = ('name', 'description', 'api_key', 'endpoint_url')
    list_filter = ('is_active', 'last_synced_at')

admin.site.register(IntegrationService, IntegrationServiceAdmin)
