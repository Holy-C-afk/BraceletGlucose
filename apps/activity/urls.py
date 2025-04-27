# filepath: c:\Users\tachf\BARCELETGLUCOSE\apps\activity\urls.py
from django.urls import path
from . import views

app_name = 'activity'

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('<int:pk>/', views.activity_detail, name='activity_detail'),
]