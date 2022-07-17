from django.urls import path

from .views import SpecialtyList, SpecialtyDetail, WorkersList, WorkerDetail


urlpatterns = [
    path("api/workers/skills/", SpecialtyList.as_view()),
    path("api/workers/skills/<int:pk>/", SpecialtyDetail.as_view()),
    path("api/workers/", WorkersList.as_view()),
    path("api/workers/<int:pk>/", WorkerDetail.as_view()),
]