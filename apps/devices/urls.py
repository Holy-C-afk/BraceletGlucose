from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'devices', views.DeviceViewSet, basename='device')
router.register(r'device-data', views.DeviceDataViewSet, basename='device-data')

urlpatterns = [
    path('', include(router.urls)),
] 