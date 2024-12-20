from rest_framework import serializers
from .models import Platform, Duty, Task

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'
        read_only_fields = ('owner',)

class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Duty
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    platform = PlatformSerializer(read_only=True)
    duty = DutySerializer(many=True, read_only=True)
    platform_id = serializers.IntegerField(write_only=True)
    duty_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('owner',)
    
    def create(self, validated_data):
        duty_ids = validated_data.pop('duty_ids', [])
        task = Task.objects.create(**validated_data)
        task.duty.set(duty_ids)
        return task