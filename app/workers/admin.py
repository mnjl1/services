from django.contrib import admin

from .models import Speciality, Worker

class SpecialityAdmin(admin.ModelAdmin):
    pass


class WorkerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Worker, WorkerAdmin)

