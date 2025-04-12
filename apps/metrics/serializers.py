from rest_framework import serializers
from .models import HealthMetrics, Alert

class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrics
        fields = [
            'id', 'date', 'average_glucose', 'min_glucose', 'max_glucose',
            'average_heart_rate', 'min_heart_rate', 'max_heart_rate',
            'average_temperature', 'total_steps', 'total_calories'
        ]
        read_only_fields = ['date']

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = [
            'id', 'alert_type', 'message', 'severity', 'status',
            'created_at', 'resolved_at'
        ]
        read_only_fields = ['created_at', 'resolved_at'] 