from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Count
from .models import Department, Employee, Performance
from .serializers import DepartmentSerializer, EmployeeSerializer, PerformanceSerializer
from .filters import EmployeeFilter, PerformanceFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class IsAuthenticatedOrReadOnly(permissions.IsAuthenticatedOrReadOnly): pass

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name','id']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EmployeeFilter
    search_fields = ['name','email','phone']
    ordering_fields = ['date_of_joining','name','id']

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.select_related('employee').all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PerformanceFilter
    ordering_fields = ['review_date','rating','id']

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def employees_per_department(request):
    data = (Department.objects
            .values('name')
            .annotate(count=Count('employees'))
            .order_by('-count'))
    return Response(list(data))

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def monthly_attendance_overview(request):
    from attendance.models import Attendance
    from django.db.models.functions import TruncMonth
    from django.db.models import Count
    qs = (Attendance.objects
          .annotate(month=TruncMonth('date'))
          .values('month','status')
          .annotate(count=Count('id'))
          .order_by('month','status'))
    return Response(list(qs))
