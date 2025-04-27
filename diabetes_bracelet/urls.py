from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.dashboard.urls', namespace='dashboard')),
    path('activity/', include('apps.activity.urls', namespace='activity')),
    path('glucose/', include('apps.glucose.urls', namespace='glucose')),
    path('insulin/', include('apps.insulin.urls', namespace='insulin')),
    path('users/', include('apps.users.urls', namespace='users')),
    path('devices/', include('apps.devices.urls', namespace='devices')),
    path('metrics/', include('apps.metrics.urls', namespace='metrics')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)