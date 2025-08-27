from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT='Present','Present'
        ABSENT='Absent','Absent'
        LATE='Late','Late'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices)

    class Meta:
        unique_together = ('employee','date')
        ordering = ['-date']
