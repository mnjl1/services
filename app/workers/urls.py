from django.urls import path

from .views import SpecialtyList, SpecialtyDetail, WorkersList, WorkerDetail


urlpatterns = [
    path("skills/", SpecialtyList.as_view()),
    path("skills/<int:pk>/", SpecialtyDetail.as_view()),
    path("", WorkersList.as_view()),
    path("<int:pk>/", WorkerDetail.as_view()),
]