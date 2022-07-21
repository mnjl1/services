from pyexpat import model
from rest_framework import serializers

from .models import Appointment
from administration.serializers import WorkerLocationJobIntervalSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    service = WorkerLocationJobIntervalSerializer()

    class Meta:
        model = Appointment
        fields = ('client_name', 'service',)