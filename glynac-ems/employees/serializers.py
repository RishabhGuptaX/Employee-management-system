from rest_framework import serializers
from .models import Department, Employee, Performance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name']

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source='department.name')
    class Meta:
        model = Employee
        fields = ['id','name','email','phone','address','date_of_joining','department','department_name']

class PerformanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.ReadOnlyField(source='employee.name')
    class Meta:
        model = Performance
        fields = ['id','employee','employee_name','rating','review_date']
