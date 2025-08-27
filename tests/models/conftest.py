import pytest
from app.models import Player, Warrior, EnumClasses, Weapon, EnumWeapon, WeaponStats


@pytest.fixture
def get_player():
    return Player()


@pytest.fixture()
def get_char_classes():
    return Warrior()


@pytest.fixture
def make_weapon():
    def _make_weapon(stats=None, chosen_weapon=EnumWeapon.SWORD, allowed=None):
        return Weapon(
            weapon_stats=stats or WeaponStats(attack=5),
            chosen_weapon=chosen_weapon,
            allowed_classes=allowed or [EnumClasses.WARRIOR, EnumClasses.ROGUE]
        )
    return _make_weapon
