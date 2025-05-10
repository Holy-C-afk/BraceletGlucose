from django.contrib import admin
from .models import GlucoseReading
# Register your models here.

@admin.register(GlucoseReading)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'value', 'timestamp','notes','device')