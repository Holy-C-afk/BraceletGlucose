from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import DashboardSettings
from apps.glucose.models import GlucoseReading
from apps.insulin.models import InsulinDose
from apps.activity.models import ActivityLog
from datetime import datetime, timedelta
import json


@login_required
def dashboard(request):
    """View for the main dashboard page."""
    # Get or create dashboard settings
    settings, created = DashboardSettings.objects.get_or_create(user=request.user)
    
    # Get date range from request or use default (last 7 days)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    # Get glucose readings
    glucose_readings = GlucoseReading.objects.filter(
        user=request.user,
        timestamp__range=(start_date, end_date)
    ).order_by('timestamp')
    
    # Get insulin doses
    insulin_doses = InsulinDose.objects.filter(
        user=request.user,
        timestamp__range=(start_date, end_date)
    ).order_by('timestamp')
    
    # Get activity logs
    activity_logs = ActivityLog.objects.filter(
        user=request.user,
        start_time__range=(start_date, end_date)
    ).order_by('start_time')
    
    context = {
        'settings': settings,
        'glucose_readings': glucose_readings,
        'insulin_doses': insulin_doses,
        'activity_logs': activity_logs,
    }
    
    return render(request, 'dashboard/dashboard.html', context)


@login_required
@require_http_methods(['POST'])
def update_settings(request):
    """Update dashboard settings."""
    try:
        settings = DashboardSettings.objects.get(user=request.user)
        data = json.loads(request.body)
        
        # Update settings
        for key, value in data.items():
            if hasattr(settings, key):
                setattr(settings, key, value)
        
        settings.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400) 