from django.db import models
from django.conf import settings


class TimeStampModel(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Speciality(TimeStampModel):
    skill = models.CharField(max_length=255)

    class Meta:
        ordering = ('skill', )

    def __str__(self):
        return f'{self.skill}'


class Worker(TimeStampModel):
    worker = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    skill = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    class Meta:
        ordering = ('worker', )

    def __str__(self):
        return f'{self.worker}, {self.specialty}'
