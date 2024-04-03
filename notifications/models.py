from django.db import models
from django.contrib.auth.models import User
from company.models import Company
from coupon.models import Coupon
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    message = models.TextField()
    sent_datetime = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username if self.user else self.company.name} - {self.coupon.code}"
