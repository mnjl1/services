import pytest
from datetime import datetime

from administration.models import Location, WorkerLocationJobInterval
from workers.models import Worker, Speciality
from accounts.models import CustomUser


@pytest.mark.django_db
def test_location_model():
    location = Location(place='AcademCityCenter')
    location.save()

    assert location.place == 'AcademCityCenter'


@pytest.mark.django_db
def test_woker_location_interval():
    location = Location(place='AcademCityCenter')
    location.save()
    massage = Speciality(skill='massage')
    massage.save()
    user = CustomUser(username='Elon', email='elon@twitter.com')
    user.save()
    worker = Worker(worker=user, skill=massage)
    worker.save()
    service = WorkerLocationJobInterval(
        location=location,
        worker=worker,
        start_time=datetime(2022, 7, 12, 10, 00, 00),
        end_time=datetime(2022, 7, 12, 12, 00, 00)
    )
    service.save()

    assert service.location.place == 'AcademCityCenter'
    assert service.worker.skill.skill == 'massage'