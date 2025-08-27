import pytest
from app.models import EnumWeapon, EnumClasses, WeaponStats


@pytest.mark.parametrize('stats, chosen_weapon, allowed', [
    (WeaponStats(attack=5), EnumWeapon.SWORD, [EnumClasses.WARRIOR, EnumClasses.ROGUE]),
    (WeaponStats(attack=3, heal=1), EnumWeapon.DAGGER, [EnumClasses.ROGUE, EnumClasses.MAGE]),
    (WeaponStats(attack=1, heal=4), EnumWeapon.STAFF, [EnumClasses.MAGE])
])
def test_create_weapons(make_weapon, stats, chosen_weapon, allowed):
    weapon = make_weapon(stats, chosen_weapon, allowed)
    assert weapon.chosen_weapon.name == chosen_weapon.name
    assert weapon.weapon_stats.attack == stats.attack
    assert weapon.weapon_stats.heal == stats.heal
    assert set(weapon.who_can_use) == set(allowed)


@pytest.mark.parametrize('stats, chosen_weapon, allowed, add_class, remove_class, list_to_verify', [
    (WeaponStats(attack=10), EnumWeapon.SWORD, [EnumClasses.WARRIOR], EnumClasses.ROGUE, None, [EnumClasses.WARRIOR, EnumClasses.ROGUE]),
    (WeaponStats(attack=7, heal=2), EnumWeapon.DAGGER, [EnumClasses.ROGUE], EnumClasses.MAGE, EnumClasses.ROGUE, [EnumClasses.MAGE]),
    (WeaponStats(attack=3, heal=11), EnumWeapon.STAFF, [EnumClasses.MAGE], None, EnumClasses.MAGE, [])
])
def test_changing_allowed_classes(make_weapon, stats, chosen_weapon, allowed, add_class, remove_class, list_to_verify):
    weapon = make_weapon(stats, chosen_weapon, allowed)
    if add_class is not None:
        weapon.add_allowed_class(add_class)
    if remove_class is not None:
        weapon.remove_allowed_class(remove_class)
    
    assert set(weapon.who_can_use) == set(list_to_verify)
