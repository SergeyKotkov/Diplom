from django.test import TestCase
from .models import Employee, Task

class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(full_name="John Doe", position="Developer")

    def test_employee_creation(self):
        employee = Employee.objects.get(full_name="John Doe")
        self.assertEqual(employee.position, "Developer")

class TaskTestCase(TestCase):
    def setUp(self):
        employee = Employee.objects.create(full_name="Jane Doe", position="Manager")
        Task.objects.create(name="Task 1", executor=employee, deadline="2023-12-31", status="not_started")

    def test_task_creation(self):
        task = Task.objects.get(name="Task 1")
        self.assertEqual(task.status, "not_started")

