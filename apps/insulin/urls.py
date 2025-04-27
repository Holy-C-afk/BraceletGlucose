from django.urls import path
from . import views

app_name = 'insulin'

urlpatterns = [
    path('', views.insulin_list, name='insulin_list'),
    path('<int:pk>/', views.insulin_detail, name='insulin_detail'),
]