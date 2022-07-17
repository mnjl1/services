import pytest

from workers.serializers import SpecialtySerializer

def test_valid_specialty_serializer():
    valid_data = {
        'skill': 'massage'
    }
    serializer = SpecialtySerializer(data=valid_data)
    serializer.is_valid()
    assert serializer.validated_data == valid_data
    assert serializer.data == valid_data
    assert serializer.errors == {}
