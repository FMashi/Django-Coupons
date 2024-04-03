from django.contrib import admin
from .models import CouponUsage

class CouponUsageAdmin(admin.ModelAdmin):
    list_display = ('coupon', 'user', 'usage_datetime')
    search_fields = ('coupon__company__name', 'coupon__code', 'user__username')
    list_filter = ('coupon__company__name', 'usage_datetime')

admin.site.register(CouponUsage, CouponUsageAdmin)
