import pytest
from rest_framework.test import APIClient
from employees.models import Department, Employee
from datetime import date

@pytest.mark.django_db
def test_employee_crud_smoke():
    dept = Department.objects.create(name='Engineering')
    client = APIClient()
    resp = client.post('/api/employees/', {
        'name':'Alice','email':'alice@example.com','phone':'','address':'','date_of_joining': str(date.today()),
        'department': dept.id
    }, format='json')
    assert resp.status_code in (200,201)
    emp_id = resp.json()['id']
    resp = client.get(f'/api/employees/{emp_id}/')
    assert resp.status_code == 200
