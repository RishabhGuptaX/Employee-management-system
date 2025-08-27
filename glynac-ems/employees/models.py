from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=120, unique=True)
    def __str__(self): return self.name

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employees')
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=40, blank=True)
    address = models.TextField(blank=True)
    date_of_joining = models.DateField()

    class Meta:
        indexes = [models.Index(fields=['email']), models.Index(fields=['name'])]
        ordering = ['-date_of_joining']

    def __str__(self): return f"{self.name} <{self.email}>"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    rating = models.PositiveSmallIntegerField()  # 1-5
    review_date = models.DateField()

    class Meta:
        ordering = ['-review_date']
