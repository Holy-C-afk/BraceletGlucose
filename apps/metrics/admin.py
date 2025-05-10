from django.contrib import admin
from .models import HealthMetrics
# Register your models here.

@admin.register(HealthMetrics)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'average_glucose', 'average_heart_rate', 'average_temperature')
    list_filter = ('user', 'date')
    search_fields = ('user__username', 'date')
    ordering = ('-date',)
    date_hierarchy = 'date'