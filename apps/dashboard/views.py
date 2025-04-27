from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.timezone import now  # Use timezone-aware datetime
from .models import DashboardSettings
from apps.glucose.models import GlucoseReading
from apps.insulin.models import InsulinDose
from apps.activity.models import ActivityLog
from datetime import timedelta
import json
import logging

logger = logging.getLogger(__name__)

@login_required
def dashboard(request):
    """View for the main dashboard page."""
    try:
        # Get or create dashboard settings
        settings, created = DashboardSettings.objects.get_or_create(user=request.user)
        
        # Get date range from request or use default (last 7 days)
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        try:
            if start_date:
                start_date = now().strptime(start_date, '%Y-%m-%d')
            else:
                start_date = now() - timedelta(days=7)
            if end_date:
                end_date = now().strptime(end_date, '%Y-%m-%d')
            else:
                end_date = now()
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)
        
        # Fetch data
        glucose_readings = GlucoseReading.objects.filter(
            user=request.user,
            timestamp__range=(start_date, end_date)
        ).order_by('timestamp')
        
        insulin_doses = InsulinDose.objects.filter(
            user=request.user,
            timestamp__range=(start_date, end_date)
        ).order_by('timestamp')
        
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
    except Exception as e:
        logger.error(f"Error loading dashboard for user {request.user.id}: {str(e)}")
        return JsonResponse({'status': 'error', 'message': f'Failed to load dashboard: {str(e)}'}, status=500)


@login_required
@require_http_methods(['POST'])
def update_settings(request):
    """Update dashboard settings."""
    try:
        settings = DashboardSettings.objects.get(user=request.user)
        data = json.loads(request.body)
        
        # Validate and update settings
        valid_fields = ['field1', 'field2', 'field3']  # Replace with actual fields in DashboardSettings
        for key, value in data.items():
            if key in valid_fields and hasattr(settings, key):
                setattr(settings, key, value)
        
        settings.save()
        return JsonResponse({'status': 'success'})
    except DashboardSettings.DoesNotExist:
        logger.error(f"Dashboard settings not found for user {request.user.id}")
        return JsonResponse({'status': 'error', 'message': 'Dashboard settings not found.'}, status=404)
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON data received for user {request.user.id}")
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data.'}, status=400)
    except Exception as e:
        logger.error(f"Error updating settings for user {request.user.id}: {str(e)}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {str(e)}'}, status=500)