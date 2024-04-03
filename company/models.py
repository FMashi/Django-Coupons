from django.db import models
import secrets

class Company(models.Model):
    registration_no = models.CharField(max_length=10, blank=True)
    identification_no = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not (self.identification_no and self.registration_no):
            self.identification_no = secrets.token_urlsafe(3).upper().replace('_', '')[:10]
            self.registration_no = int(secrets.token_urlsafe(3), 36)
        super().save(*args, **kwargs)