from datetime import datetime
from rest_framework import serializers
from .models import Employee, Task, TeamLeader


class TeamLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLeader
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_full_name(self, value):
        if not value:
            raise serializers.ValidationError("Требуется полное имя.")
        return value

    def validate_task(self, value):
        if self.instance and self.instance.task and self.instance.task != value:
            raise serializers.ValidationError("Этому сотруднику уже назначена задача.")
        return value

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, value):
        if value < datetime.today().date():
            raise serializers.ValidationError("Срок не может быть в прошлом.")
        return value