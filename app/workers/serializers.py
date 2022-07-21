from rest_framework import serializers

from accounts.serializers import CustomUserSerializer
from .models import Worker, Speciality


class SpecialtySerializer(serializers.ModelSerializer):

    class Meta:
        model = Speciality
        fields = ('skill',)


class WorkerSerializer(serializers.ModelSerializer):
    worker = CustomUserSerializer()
    skill = SpecialtySerializer()

    class Meta:
        model = Worker
        fields = ('worker', 'skill',)
        read_only_fields = ('id', 'created', 'last_modified',)