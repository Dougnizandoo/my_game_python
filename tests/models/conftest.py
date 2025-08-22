import pytest
from app.models import Player, Warrior


@pytest.fixture
def get_player():
    return Player()


@pytest.fixture(params=[Warrior])
def get_char_classes(request):
    return Warrior()
