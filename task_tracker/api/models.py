from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)


    def __str__(self):
        return self.full_name

class Task(models.Model):
    name = models.CharField(max_length=255)
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    executor = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deadline = models.DateField()
    status = models.CharField(max_length=50)


    def __str__(self):
        return self.name

