from django.db import models

class IntegrationService(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    api_key = models.CharField(max_length=100, blank=True, null=True)
    endpoint_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    authentication_type = models.CharField(max_length=50, blank=True, null=True)
    timeout_seconds = models.PositiveIntegerField(default=30)
    last_synced_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name