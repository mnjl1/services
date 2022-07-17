import pytest

from workers.models import Speciality


@pytest.fixture(scope='function')
def add_skill():
    def _add_skill(skill):
        skill = Speciality.objects.create(skill=skill)
        return skill
    return _add_skill


@pytest.mark.django_db
def test_add_specialty(client):
    skills = Speciality.objects.all()
    assert len(skills) == 0

    resp = client.post(
        "/api/workers/skills/",
        {
            'skill': 'massage'
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["skill"] == "massage"

    skills = Speciality.objects.all()
    assert len(skills) == 1


@pytest.mark.django_db
def test_get_single_specialty(client, add_skill):
    skill = add_skill(skill="massage")
    resp = client.get(f"/api/workers/skills/{skill.id}/")
    assert resp.status_code == 200
    assert resp.data["skill"] == "massage"


@pytest.mark.django_db
def test_get_all_skills(client, add_skill):
    skill1 = add_skill(skill="dev")
    skill2 = add_skill(skill="massage")
    resp = client.get(f"/api/workers/skills/")
    print(resp.data[0]["skill"])
    assert resp.status_code == 200
    assert resp.data[0]["skill"] == skill1.skill
    assert resp.data[1]["skill"] == skill2.skill