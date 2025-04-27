from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # URL for the main dashboard page
    path('update-settings/', views.update_settings, name='update_settings'),  # URL for updating dashboard settings
]