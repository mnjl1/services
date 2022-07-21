from pyexpat import model
from rest_framework import serializers
from workers.serializers import WorkerSerializer
from .models import Location, WorkerLocationJobInterval


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('location',)


class WorkerLocationJobIntervalSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    worker = WorkerSerializer()
    class Meta:
        model = WorkerLocationJobInterval
        fields = (
            'location',
            'worker',
            'start_time',
            'end_time'
        )