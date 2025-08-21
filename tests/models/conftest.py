import pytest
from app.models import Player


@pytest.fixture
def get_player():
    return Player()
