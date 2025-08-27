from django.contrib import admin
from .models import Department, Employee, Performance

admin.site.register(Department)
class PerformanceInline(admin.TabularInline):
    model = Performance
    extra = 0
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','department','date_of_joining')
    search_fields = ('name','email')
    list_filter = ('department',)
    inlines = [PerformanceInline]
