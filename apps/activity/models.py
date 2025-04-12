from django.db import models
from django.conf import settings

class ActivityLog(models.Model):
    ACTIVITY_TYPES = [
        ('walking', 'Walking'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('gym', 'Gym workout'),
        ('other', 'Other'),
    ]

    INTENSITY_LEVELS = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    intensity = models.CharField(max_length=10, choices=INTENSITY_LEVELS)
    duration = models.DurationField()
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    device = models.ForeignKey('devices.Device', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-start_time']

    def __str__(self):
        return f"{self.get_activity_type_display()} for {self.duration} at {self.start_time}"

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = self.start_time + self.duration
        super().save(*args, **kwargs)
