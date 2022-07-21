from django.urls import path

from .views import LocationList, WorkerJobIntervalList


urlpatterns = [
    path('locations/', LocationList.as_view()),
    path('job-intervals/', WorkerJobIntervalList.as_view())
]