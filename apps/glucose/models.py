from django.db import models
from django.conf import settings

# Create your models here.

class GlucoseReading(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    device = models.ForeignKey('devices.Device', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.value} mg/dL at {self.timestamp}"
