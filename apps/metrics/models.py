from django.db import models
from django.conf import settings
from apps.devices.models import DeviceData

class HealthMetrics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='health_metrics')
    date = models.DateField(auto_now_add=True)
    average_glucose = models.FloatField()
    min_glucose = models.FloatField()
    max_glucose = models.FloatField()
    average_heart_rate = models.FloatField()
    min_heart_rate = models.IntegerField()
    max_heart_rate = models.IntegerField()
    average_temperature = models.FloatField()
    total_steps = models.IntegerField()
    total_calories = models.FloatField()
    
    class Meta:
        verbose_name = 'Daily Health Metrics'
        verbose_name_plural = 'Daily Health Metrics'
        ordering = ['-date']
    
    def __str__(self):
        return f"Health Metrics for {self.user.get_full_name()} on {self.date}"
    
    @classmethod
    def calculate_daily_metrics(cls, user, date):
        """Calculate daily health metrics from device data"""
        device_data = DeviceData.objects.filter(
            device__user=user,
            timestamp__date=date
        )
        
        if not device_data.exists():
            return None
        
        metrics = {
            'average_glucose': device_data.aggregate(models.Avg('glucose_level'))['glucose_level__avg'],
            'min_glucose': device_data.aggregate(models.Min('glucose_level'))['glucose_level__min'],
            'max_glucose': device_data.aggregate(models.Max('glucose_level'))['glucose_level__max'],
            'average_heart_rate': device_data.aggregate(models.Avg('heart_rate'))['heart_rate__avg'],
            'min_heart_rate': device_data.aggregate(models.Min('heart_rate'))['heart_rate__min'],
            'max_heart_rate': device_data.aggregate(models.Max('heart_rate'))['heart_rate__max'],
            'average_temperature': device_data.aggregate(models.Avg('temperature'))['temperature__avg'],
            'total_steps': device_data.aggregate(models.Sum('steps'))['steps__sum'],
            'total_calories': device_data.aggregate(models.Sum('calories'))['calories__sum'],
        }
        
        return cls.objects.create(user=user, **metrics)

class Alert(models.Model):
    SEVERITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )
    
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('acknowledged', 'Acknowledged'),
        ('resolved', 'Resolved'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='alerts')
    device_data = models.ForeignKey(DeviceData, on_delete=models.CASCADE, related_name='alerts')
    alert_type = models.CharField(max_length=50)
    message = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Alert'
        verbose_name_plural = 'Alerts'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.alert_type} Alert for {self.user.get_full_name()} at {self.created_at}"
    
    @classmethod
    def check_device_data(cls, device_data):
        """Check device data for potential alerts"""
        alerts = []
        
        # Check glucose levels
        if device_data.glucose_level < 70:
            alerts.append(cls(
                user=device_data.device.user,
                device_data=device_data,
                alert_type='Low Glucose',
                message=f'Glucose level is too low: {device_data.glucose_level} mg/dL',
                severity='high'
            ))
        elif device_data.glucose_level > 180:
            alerts.append(cls(
                user=device_data.device.user,
                device_data=device_data,
                alert_type='High Glucose',
                message=f'Glucose level is too high: {device_data.glucose_level} mg/dL',
                severity='high'
            ))
        
        # Check heart rate
        if device_data.heart_rate < 60:
            alerts.append(cls(
                user=device_data.device.user,
                device_data=device_data,
                alert_type='Low Heart Rate',
                message=f'Heart rate is too low: {device_data.heart_rate} BPM',
                severity='medium'
            ))
        elif device_data.heart_rate > 100:
            alerts.append(cls(
                user=device_data.device.user,
                device_data=device_data,
                alert_type='High Heart Rate',
                message=f'Heart rate is too high: {device_data.heart_rate} BPM',
                severity='medium'
            ))
        
        # Check temperature
        if device_data.temperature < 36.5:
            alerts.append(cls(
                user=device_data.device.user,
                device_data=device_data,
                alert_type='Low Temperature',
                message=f'Body temperature is too low: {device_data.temperature}°C',
                severity='medium'
            ))
        elif device_data.temperature > 37.5:
            alerts.append(cls(
                user=device_data.device.user,
                device_data=device_data,
                alert_type='High Temperature',
                message=f'Body temperature is too high: {device_data.temperature}°C',
                severity='medium'
            ))
        
        return alerts 