import pytest
from mixer.backend.django import mixer

# write to DB
pytestmark = pytest.mark.django_db


def test_message():
    obj = mixer.blend('simple_app.Message')
    assert obj.pk > 0