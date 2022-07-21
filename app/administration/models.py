from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

from workers.models import TimeStampModel, Worker
from datetime import datetime

from .utils import overlap


class WorkerLocationJobIntervalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            start_time__gte = datetime.now()
            ).filter(
                is_reserved=False
            )


class Location(TimeStampModel):
    """
    Worker locations
    """
    location = models.CharField(max_length=255)

    class Meta:
        ordering = ('location', )

    def __str__(self):
        return f'{self.location}'

class WorkerLocationJobInterval(TimeStampModel):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_reserved = models.BooleanField(default=False)

    objects = models.Manager()
    free_for_appontment_objects = WorkerLocationJobIntervalManager()

    def __str__(self):
        return f'{self.location}, {self.worker}, {self.start_time}, {self.end_time}'


@receiver(pre_save, sender=WorkerLocationJobInterval)
def check_worker_is_available(sender, instance, *args, **kwargs):
    """
    Check before saving model if it is unique
    """
    active_intervals = WorkerLocationJobInterval.objects.filter(
        start_time__gte = datetime.now()
    )
    start = instance.start_time
    end = instance.end_time

    for interval in active_intervals:
        i1 = interval.start_time
        i2 = interval.end_time

        if interval.location == instance.location:
            if interval.worker == instance.worker:
                if not overlap(start, end, i1) and not overlap(start, end, i2):
                    pass
                else:
                    raise Exception('Object saving restriction')

        
        

            




    
    


