from calendar import TUESDAY, weekday
from django.db import models
from workers.models import TimeStampModel, Worker
from administration.models import WorkerLocationJobInterval


class Appointment(TimeStampModel):
    client_name = models.CharField(max_length=255)
    service = models.ForeignKey(WorkerLocationJobInterval, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.client_name}, {self.service}'
    