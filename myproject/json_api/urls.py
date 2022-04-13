
from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# JWT Auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




# Authentication 

# Basic AUTHENTICATION  
# username , password


# Session Authentication


# TOKEN AUTHENTICATION
# Stored in Database


# JWT TOKEN Authentication
