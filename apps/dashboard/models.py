from django.db import models
from django.conf import settings


class DashboardSettings(models.Model):
    """Model for storing user dashboard preferences."""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='dashboard_settings'
    )
    theme = models.CharField(
        max_length=20,
        choices=[
            ('light', 'Light'),
            ('dark', 'Dark'),
            ('system', 'System')
        ],
        default='system'
    )
    show_glucose_chart = models.BooleanField(default=True)
    show_insulin_chart = models.BooleanField(default=True)
    show_activity_chart = models.BooleanField(default=True)
    glucose_unit = models.CharField(
        max_length=10,
        choices=[
            ('mg/dL', 'mg/dL'),
            ('mmol/L', 'mmol/L')
        ],
        default='mg/dL'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Dashboard Settings'
        verbose_name_plural = 'Dashboard Settings'

    def __str__(self):
        return f"Dashboard Settings for {self.user.username}" 