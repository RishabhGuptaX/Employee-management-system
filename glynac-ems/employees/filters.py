import django_filters
from .models import Employee, Performance

class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.NumberFilter(field_name='department__id')
    date_joined_after = django_filters.DateFilter(field_name='date_of_joining', lookup_expr='gte')
    date_joined_before = django_filters.DateFilter(field_name='date_of_joining', lookup_expr='lte')
    class Meta:
        model = Employee
        fields = ['department','date_joined_after','date_joined_before']

class PerformanceFilter(django_filters.FilterSet):
    employee = django_filters.NumberFilter(field_name='employee__id')
    min_rating = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    class Meta:
        model = Performance
        fields = ['employee','min_rating','max_rating']
