from rest_framework import serializers
from .models import Device, DeviceData

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'id', 'device_id', 'name', 'status', 'battery_level',
            'last_sync', 'firmware_version', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class DeviceDataSerializer(serializers.ModelSerializer):
    is_glucose_normal = serializers.BooleanField(read_only=True)
    is_heart_rate_normal = serializers.BooleanField(read_only=True)
    is_temperature_normal = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = DeviceData
        fields = [
            'id', 'device', 'timestamp', 'glucose_level', 'heart_rate',
            'temperature', 'blood_oxygen', 'steps', 'calories',
            'is_glucose_normal', 'is_heart_rate_normal', 'is_temperature_normal'
        ]
        read_only_fields = ['timestamp'] 