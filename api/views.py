# api/views.py

from rest_framework import generics
from analytics.models import CouponUsage
from company.models import Company
from coupon.models import Coupon
from integration.models import IntegrationService
from notifications.models import Notification
from .serializers import (
    CompanySerializer,
    CouponSerializer,
    CouponUsageSerializer,
    NotificationSerializer,
    IntegrationServiceSerializer,
)

class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CouponListCreateAPIView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class CouponDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class CouponUsageListCreateAPIView(generics.ListCreateAPIView):
    queryset = CouponUsage.objects.all()
    serializer_class = CouponUsageSerializer

class CouponUsageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CouponUsage.objects.all()
    serializer_class = CouponUsageSerializer

class NotificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class IntegrationServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = IntegrationService.objects.all()
    serializer_class = IntegrationServiceSerializer

class IntegrationServiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IntegrationService.objects.all()
    serializer_class = IntegrationServiceSerializer

