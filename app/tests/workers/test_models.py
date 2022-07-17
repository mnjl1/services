import pytest

from workers.models import Speciality, Worker
from accounts.models import CustomUser

@pytest.mark.django_db
def test_speciality_model():
    skill = Speciality(skill='massage')
    skill.save()

    assert skill.skill == 'massage'


@pytest.mark.django_db
def test_worker_model():
    massage = Speciality(skill='massage')
    massage.save()
    user = CustomUser(username='Elon', email='elon@twitter.com')
    user.save()
    worker = Worker(worker=user, skill=massage)
    worker.save()
    assert worker.skill.skill== 'massage'