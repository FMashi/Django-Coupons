from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from company.models import Company


GENDER = [
    ('M', _('Male')),
    ('F', _('Female')),
] 


class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    # profile_image = models.ImageField(upload_to='images/profiles/', blank=True, null=True)
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        
    def __str__(self):
        return self.username
    
