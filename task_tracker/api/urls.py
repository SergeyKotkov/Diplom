from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, TaskViewSet, busy_employees, important_tasks

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('busy_employees/', busy_employees, name='busy_employees'),
    path('important_tasks/', important_tasks, name='important_tasks'),
]





