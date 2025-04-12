from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Device, DeviceData
from .serializers import DeviceSerializer, DeviceDataSerializer
from apps.metrics.models import Alert

class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def sync_data(self, request, pk=None):
        device = self.get_object()
        
        # Simulate device data (replace with actual device communication)
        data = {
            'glucose_level': request.data.get('glucose_level', 100),
            'heart_rate': request.data.get('heart_rate', 75),
            'temperature': request.data.get('temperature', 37.0),
            'blood_oxygen': request.data.get('blood_oxygen', 98),
            'steps': request.data.get('steps', 0),
            'calories': request.data.get('calories', 0),
        }
        
        device_data = DeviceData.objects.create(device=device, **data)
        
        # Check for alerts
        alerts = Alert.check_device_data(device_data)
        for alert in alerts:
            alert.save()
        
        # Update device status
        device.last_sync = timezone.now()
        device.save()
        
        return Response({
            'status': 'success',
            'device_data': DeviceDataSerializer(device_data).data,
            'alerts': len(alerts)
        })
    
    @action(detail=True, methods=['get'])
    def data_history(self, request, pk=None):
        device = self.get_object()
        days = int(request.query_params.get('days', 7))
        
        data = DeviceData.objects.filter(
            device=device,
            timestamp__gte=timezone.now() - timezone.timedelta(days=days)
        ).order_by('timestamp')
        
        serializer = DeviceDataSerializer(data, many=True)
        return Response(serializer.data)

class DeviceDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DeviceDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return DeviceData.objects.filter(device__user=self.request.user) 