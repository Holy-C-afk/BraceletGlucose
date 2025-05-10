from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type', 'date_of_birth', 'phone_number','address','emergency_phone', 'emergency_contact')