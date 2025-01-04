from datetime import datetime
from rest_framework import serializers
from .models import Employee, Task

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_full_name(self, value):
        if not value:
            raise serializers.ValidationError("Full name is required.")
        return value

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, value):
        if value < datetime.today().date():
            raise serializers.ValidationError("Deadline cannot be in the past.")
        return value