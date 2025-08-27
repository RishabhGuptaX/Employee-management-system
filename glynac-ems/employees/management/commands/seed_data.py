from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import date, timedelta
from employees.models import Department, Employee, Performance
from attendance.models import Attendance

class Command(BaseCommand):
    help = 'Seed database with fake departments, employees, attendance, and performance data.'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=50, help='Number of employees to create')

    def handle(self, *args, **opts):
        fake = Faker()
        dept_names = ['Engineering','HR','Sales','Marketing','Finance','Support']
        depts = [Department.objects.get_or_create(name=name)[0] for name in dept_names]

        count = opts['count']
        employees = []
        for _ in range(count):
            dept = random.choice(depts)
            emp = Employee.objects.create(
                department=dept,
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-3y', end_date='today')
            )
            employees.append(emp)

        statuses = ['Present','Absent','Late']
        today = date.today()
        for emp in employees:
            for i in range(90):
                if random.random() < 0.6:
                    dt = today - timedelta(days=i)
                    Attendance.objects.create(
                        employee=emp,
                        date=dt,
                        status=random.choices(statuses, weights=[80,10,10])[0]
                    )

        for emp in employees:
            for _ in range(random.randint(1, 4)):
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1,5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(employees)} employees."))
