from django.urls import path

from Auth.views import LoginApi, RegisterApi, ProfileApi

urlpatterns = [
    path('api/v0/login', LoginApi.as_view(), name='login'),
    path('api/v0/register', RegisterApi.as_view(), name='register'),
    path('api/v0/profile', ProfileApi.as_view(), name='profile'),
]
