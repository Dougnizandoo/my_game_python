import pytest
from app.models import StatusBoost, EnumStatus, EnumConsumables, EnumClasses



def test_default_consumable(make_consumable):
    cons = make_consumable()
    assert cons.name == "POTION"
    assert EnumStatus.HP in cons.effects.modifiers
    assert cons.effects.modifiers[EnumStatus.HP] == 3


@pytest.mark.parametrize('chosen_cons, allowed_classes, cons_effects', [
    (EnumConsumables.POTION, list(EnumClasses), StatusBoost({EnumStatus.HP: 2, EnumStatus.ATTACK: 1})),
    (EnumConsumables.FOOD, list(EnumClasses), StatusBoost({EnumStatus.HP: 5})),
    (EnumConsumables.POTION, [EnumClasses.WARRIOR], StatusBoost({EnumStatus.DEFENSE: 3, EnumStatus.ATTACK: 1}))
])
def test_create_consumable(make_consumable, chosen_cons, allowed_classes, cons_effects):
    potion = make_consumable(chosen_cons, allowed_classes, cons_effects)
    assert potion.name == chosen_cons.name
    assert set(potion.who_can_use) == set(allowed_classes)
    assert potion.effects.modifiers == cons_effects.modifiers
    parts = [f"{status.name}: {value}" for status, value in cons_effects.modifiers.items()]
    assert potion.description == f"This item will raise: {', '.join(parts)}"


def test_consumable_status_independence(make_consumable):
    potion = make_consumable(EnumConsumables.POTION, list(EnumClasses), StatusBoost({EnumStatus.HP: 2, EnumStatus.ATTACK: 1}))
    food = make_consumable(EnumConsumables.FOOD, list(EnumClasses), StatusBoost({EnumStatus.HP: 5}))

    potion.effects.modifiers[EnumStatus.ATTACK] = 99

    assert food.effects.modifiers[EnumStatus.HP] == 5
    assert EnumStatus.ATTACK not in food.effects.modifiers
