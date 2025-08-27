import django_filters
from .models import Attendance

class AttendanceFilter(django_filters.FilterSet):
    employee = django_filters.NumberFilter(field_name='employee__id')
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
    class Meta:
        model = Attendance
        fields = ['employee','date_from','date_to','status']
