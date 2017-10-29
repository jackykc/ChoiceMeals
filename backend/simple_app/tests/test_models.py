import pytest
from mixer.backend.django import mixer

# write to DB
pytestmark = pytest.mark.django_db


def test_ingredient():
    obj = mixer.blend('simple_app.Ingredient')
    assert obj.pk > 0