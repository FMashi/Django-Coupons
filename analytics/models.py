from django.db import models
from coupon.models import Coupon
from django.conf import settings

class CouponUsage(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    usage_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.coupon.company.name} - {self.coupon.code} used by {self.user.username} at {self.usage_datetime}"
