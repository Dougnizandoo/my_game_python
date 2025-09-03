import pytest
from app.models import Warrior, Weapon, Armor, Consumable
from app.models import EnumArmor, EnumWeapon, EnumConsumables
from app.models import WeaponStats
from app.models import Enemy, Player

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


@pytest.fixture
def make_enemy():
    def _make_enemy(enemy_type=None, enemy_hp=None, enemy_attack=None, enemy_defense=None):
        return Enemy(
            enemy_type=enemy_type,
            enemy_hp=enemy_hp,
            enemy_attack=enemy_attack,
            enemy_defense=enemy_defense
        )
    return _make_enemy

