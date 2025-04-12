from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import HealthMetrics, Alert
from .serializers import HealthMetricsSerializer, AlertSerializer

class HealthMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HealthMetricsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return HealthMetrics.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        today = timezone.now().date()
        metrics = HealthMetrics.objects.filter(
            user=request.user,
            date=today
        ).first()
        
        if not metrics:
            metrics = HealthMetrics.calculate_daily_metrics(request.user, today)
        
        if metrics:
            serializer = self.get_serializer(metrics)
            return Response(serializer.data)
        return Response(
            {'message': 'No metrics available for today'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    @action(detail=False, methods=['get'])
    def trends(self, request):
        days = int(request.query_params.get('days', 30))
        metrics = HealthMetrics.objects.filter(
            user=request.user,
            date__gte=timezone.now().date() - timezone.timedelta(days=days)
        ).order_by('date')
        
        serializer = self.get_serializer(metrics, many=True)
        return Response(serializer.data)

class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        alert = self.get_object()
        alert.status = 'acknowledged'
        alert.save()
        return Response({'status': 'alert acknowledged'})
    
    @action(detail=True, methods=['post'])
    def resolve(self, request, pk=None):
        alert = self.get_object()
        alert.status = 'resolved'
        alert.resolved_at = timezone.now()
        alert.save()
        return Response({'status': 'alert resolved'})
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        alerts = Alert.objects.filter(
            user=request.user,
            status='active'
        ).order_by('-created_at')
        
        serializer = self.get_serializer(alerts, many=True)
        return Response(serializer.data) 