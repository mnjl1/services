import pytest

from workers.models import Speciality, Worker
from accounts.models import CustomUser

@pytest.mark.django_db
def test_speciality_model():
    speciality = Speciality(skill='massage')
    speciality.save()

    assert speciality.skill == 'massage'


@pytest.mark.django_db
def test_worker_model():
    massage = Speciality(skill='massage')
    massage.save()
    user = CustomUser(username='Elon', email='elon@twitter.com')
    user.save()
    worker = Worker(worker=user, specialty=massage)
    worker.save()
    assert worker.specialty.skill== 'massage'