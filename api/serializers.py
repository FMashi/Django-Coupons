# api/serializers.py
from rest_framework import serializers
from analytics.models import CouponUsage
from company.models import Company
from coupon.models import Coupon
from integration.models import IntegrationService
from notifications.models import Notification
from authentication.models import CustomUser


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'



class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
        
class CouponUsageSerializer(serializers.ModelSerializer):
    coupon = CouponSerializer()

    class Meta:
        model = CouponUsage
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class IntegrationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationService
        fields = '__all__'
        
class CustomUserSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = CustomUser
        fields = '__all__'