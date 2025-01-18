from django.db import models

class TeamLeader(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    executor = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='executed_tasks')
    deadline = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    team_leader = models.ForeignKey(TeamLeader, null=True, blank=True, on_delete=models.SET_NULL, related_name='team_members')
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_employees')

    def __str__(self):
        return self.full_name
