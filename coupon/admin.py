from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'company', 'valid_from', 'valid_to', 'max_usage')
    search_fields = ('code', 'company__name', 'description')
    list_filter = ('valid_from', 'valid_to', 'max_usage')

admin.site.register(Coupon, CouponAdmin)
