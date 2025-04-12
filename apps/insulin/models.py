from django.db import models
from django.conf import settings

# Create your models here.

class InsulinDose(models.Model):
    INSULIN_TYPES = [
        ('rapid', 'Rapid-acting'),
        ('short', 'Short-acting'),
        ('intermediate', 'Intermediate-acting'),
        ('long', 'Long-acting'),
        ('mix', 'Mixed insulin'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    insulin_type = models.CharField(max_length=20, choices=INSULIN_TYPES)
    units = models.DecimalField(max_digits=5, decimal_places=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    device = models.ForeignKey('devices.Device', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.units} units of {self.get_insulin_type_display()} at {self.timestamp}"
