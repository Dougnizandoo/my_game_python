import pytest
from app.models import Player, Warrior, Weapon, EnumWeapon, WeaponStats, Armor, EnumArmor
from app.models import Consumable, EnumConsumables

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
            allowed_classes=allowed
        )
    return _make_weapon


@pytest.fixture
def make_armor():
    def _make_armor(armor_chosen = None, allowed_classes = None, armor_status= None):
        return Armor(
            armor_chosen= armor_chosen or EnumArmor.ARMOR,
            allowed_classes=allowed_classes,
            armor_stats=armor_status
        )
    return _make_armor


@pytest.fixture
def make_consumable():
    def _make_consumable(chosen_item = None, allowed_classes = None, consumable_effects = None):
        return Consumable(
            chosen_item=chosen_item or EnumConsumables.POTION,
            allowed_classes= allowed_classes,
            consumable_effects= consumable_effects
        )
    return _make_consumable
