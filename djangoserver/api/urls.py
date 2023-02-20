from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('marketfeed', views.market_feed, basename='market-feed')

urlpatterns = [
    path('', include(router.urls)),
    # path('marketfeed/', views.market_feed, name='market-feed')
]
