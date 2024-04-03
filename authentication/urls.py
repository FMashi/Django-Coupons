from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    user_list, 
    user_details,
    register_user,
    user_login,
    user_logout,
    change_password,
    )


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_details, name='user_details'),
    path('register/', register_user, name='register_user'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
]