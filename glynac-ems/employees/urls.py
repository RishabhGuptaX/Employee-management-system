from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DepartmentViewSet, EmployeeViewSet, PerformanceViewSet, employees_per_department, monthly_attendance_overview

router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)
router.register('performance', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reports/employees-per-department/', employees_per_department),
    path('reports/monthly-attendance/', monthly_attendance_overview),
]
