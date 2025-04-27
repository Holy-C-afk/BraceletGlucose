from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'metrics'



router = DefaultRouter()
router.register(r'health-metrics', views.HealthMetricsViewSet, basename='health-metrics')
router.register(r'alerts', views.AlertViewSet, basename='alert')

urlpatterns = [
    path('', include(router.urls)),
] 