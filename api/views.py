from rest_framework import viewsets
from .models import Employee, Task, TeamLeader
from .serializers import EmployeeSerializer, TaskSerializer, TeamLeaderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TeamLeaderViewSet(viewsets.ModelViewSet):
    queryset = TeamLeader.objects.all()
    serializer_class = TeamLeaderSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['GET'])
def busy_employees(request):
    employees = Employee.objects.annotate(task_count=Count('task')).order_by('-task_count')
    data = [{'full_name': emp.full_name, 'task_count': emp.task_count} for emp in employees]
    return Response(data)

@api_view(['GET'])
def important_tasks(request):
    important_tasks = Task.objects.filter(status='not_started', parent_task__isnull=False)
    data = []
    for task in important_tasks:
        least_busy_employee = Employee.objects.annotate(task_count=Count('task')).order_by('task_count').first()
        parent_executor = task.parent_task.executor
        if parent_executor.task_set.count() <= least_busy_employee.task_set.count() + 2:
            data.append({'task': task.name, 'deadline': task.deadline, 'employees': [parent_executor.full_name]})
        else:
            data.append({'task': task.name, 'deadline': task.deadline, 'employees': [least_busy_employee.full_name]})
    return Response(data)

@api_view(['GET'])
def important_tasks(request):
    important_tasks = Task.objects.filter(status='important')
    data = []
    for task in important_tasks:
        data.append({
            'task_name': task.name,
            'executor': task.executor.full_name if task.executor else 'No executor',
            'deadline': task.deadline,
            'status': task.status,
        })
    return Response(data)