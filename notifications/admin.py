from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'coupon', 'sent_datetime', 'is_read')
    search_fields = ('user__username', 'company__name', 'coupon__code', 'message')
    list_filter = ('is_read', 'sent_datetime')

admin.site.register(Notification, NotificationAdmin)
