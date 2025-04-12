from django.db import models
from django.conf import settings

class Device(models.Model):
    DEVICE_STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance'),
        ('defective', 'Defective'),
    )
    
    device_id = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES, default='active')
    battery_level = models.IntegerField(default=100)
    last_sync = models.DateTimeField(auto_now=True)
    firmware_version = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.device_id})"
    
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

class DeviceData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='data_points')
    timestamp = models.DateTimeField(auto_now_add=True)
    glucose_level = models.FloatField(help_text="Blood glucose level in mg/dL")
    heart_rate = models.IntegerField(help_text="Heart rate in BPM")
    temperature = models.FloatField(help_text="Body temperature in °C")
    blood_oxygen = models.IntegerField(help_text="Blood oxygen level in %", null=True, blank=True)
    steps = models.IntegerField(default=0)
    calories = models.FloatField(default=0)
    
    class Meta:
        verbose_name = 'Device Data'
        verbose_name_plural = 'Device Data'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"Data from {self.device.name} at {self.timestamp}"
    
    @property
    def is_glucose_normal(self):
        """Check if glucose level is within normal range (70-180 mg/dL)"""
        return 70 <= self.glucose_level <= 180
    
    @property
    def is_heart_rate_normal(self):
        """Check if heart rate is within normal range (60-100 BPM)"""
        return 60 <= self.heart_rate <= 100
    
    @property
    def is_temperature_normal(self):
        """Check if temperature is within normal range (36.5-37.5 °C)"""
        return 36.5 <= self.temperature <= 37.5 