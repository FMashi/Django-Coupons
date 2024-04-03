from django.urls import path
from .views import (
    CompanyListCreateAPIView,
    CompanyDetailAPIView,

    CouponListCreateAPIView,
    CouponDetailAPIView,
    CouponUsageListCreateAPIView,
    CouponUsageDetailAPIView,
    NotificationListCreateAPIView,
    NotificationDetailAPIView,
    IntegrationServiceListCreateAPIView,
    IntegrationServiceDetailAPIView,

)

urlpatterns = [
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view(), name='company-detail'),

    path('coupons/', CouponListCreateAPIView.as_view(), name='coupon-list'),
    path('coupons/<int:pk>/', CouponDetailAPIView.as_view(), name='coupon-detail'),

    path('coupon-usages/', CouponUsageListCreateAPIView.as_view(), name='coupon-usage-list'),
    path('coupon-usages/<int:pk>/', CouponUsageDetailAPIView.as_view(), name='coupon-usage-detail'),

    path('notifications/', NotificationListCreateAPIView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetailAPIView.as_view(), name='notification-detail'),

    path('integration-services/', IntegrationServiceListCreateAPIView.as_view(), name='integration-service-list'),
    path('integration-services/<int:pk>/', IntegrationServiceDetailAPIView.as_view(), name='integration-service-detail'),

]
