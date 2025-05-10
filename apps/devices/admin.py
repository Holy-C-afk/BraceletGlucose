from django.contrib import admin
from .models import Device
# Register your models here.

@admin.register(Device)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'status', 'last_sync','firmware_version')
    list_filter = ('user', 'status')    
    search_fields = ('user__username', 'name')
    ordering = ('-last_sync',)