from django.contrib import admin
from .models import InsulinDose
# Register your models here.

@admin.register(InsulinDose)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'insulin_type','units', 'timestamp', 'notes', 'device')
    list_filter = ('user', 'insulin_type', 'units', 'timestamp', 'notes', 'device')
    search_fields = ('user__username', 'insulin_type', 'units', 'timestamp', 'notes', 'device')
    ordering = ('-timestamp',)