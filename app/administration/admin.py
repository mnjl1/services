from django.contrib import admin

from .models import Location, WorkerLocationJobInterval

class LocationAdmin(admin.ModelAdmin):
    pass


class WorkerLocationJobIntervalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
admin.site.register(WorkerLocationJobInterval, WorkerLocationJobIntervalAdmin)

