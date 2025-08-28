import pytest
from app.models import ArmorStats, EnumStatus, EnumArmor, EnumClasses



@pytest.mark.parametrize('chosen_armor, stats, allowed_classes', [
    (EnumArmor.ARMOR, (5, {EnumStatus.DEFENSE: 2}), [EnumClasses.WARRIOR]),
    (EnumArmor.HOOD, (2, {EnumStatus.ATTACK: 3}), [EnumClasses.ROGUE, EnumClasses.MAGE]),
    (EnumArmor.TUNIC, (3, {EnumStatus.HP: 10}), [EnumClasses.MAGE])
])
def test_create_armor(make_armor, chosen_armor, stats, allowed_classes):
    status = ArmorStats(defense=stats[0], status_to_upgrade=stats[1])
    armor = make_armor(chosen_armor, allowed_classes, status)

    assert armor.name == chosen_armor.name
    assert armor.armor_stats.defense == status.defense
    assert armor.armor_stats.status_to_upgrade == status.status_to_upgrade
    assert set(armor.who_can_use) == set(allowed_classes)



def test_armor_status_independence(make_armor):
    armor1 = make_armor(EnumArmor.ARMOR, [EnumClasses.WARRIOR], ArmorStats(defense=5, status_to_upgrade={EnumStatus.HP: 10}))
    armor2 = make_armor(EnumArmor.HOOD, [EnumClasses.MAGE], ArmorStats(defense=2, status_to_upgrade={EnumStatus.DEFENSE: 3}))

    # modificando o primeiro
    armor1.armor_stats.status_to_upgrade[EnumStatus.HP] = 99

    # garante que não afetou o segundo
    assert armor2.armor_stats.status_to_upgrade[EnumStatus.DEFENSE] == 3
    assert EnumStatus.HP not in armor2.armor_stats.status_to_upgrade
