from django.contrib import admin
from .models import Employee, TeamLeader, Task

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'team_leader']
    list_filter = ['position', 'team_leader']
    search_fields = ['full_name', 'position']

@admin.register(TeamLeader)
class TeamLeaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
    search_fields = ['name', 'department']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'parent_task', 'executor', 'deadline', 'status']