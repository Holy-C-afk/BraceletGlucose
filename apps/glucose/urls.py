from django.urls import path
from . import views

app_name = 'glucose'

urlpatterns = [
    path('', views.glucose_list, name='glucose_list'),
    path('<int:pk>/', views.glucose_detail, name='glucose_detail'),
]