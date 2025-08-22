import pytest
from tests.models.helper import assert_attrs


@pytest.mark.parametrize('attr_expected', [
    {
        "class_name": "Warrior",
        "special_attack": {"name": "shield-breaker", "attack": 2, "heal": 0},
        "levelup_points": {"hp": 1, "attack": 1, "defense": 2}
    }
])
def test_get_class_stats(get_player, get_char_classes, attr_expected):
    player = get_player
    player.current_class = get_char_classes

    pClass = player.current_class

    assert pClass.class_name == attr_expected["class_name"]

    # Special attack
    assert_attrs(pClass.special_attack, attr_expected["special_attack"])

    # Levelup points
    assert_attrs(pClass.levelup_points, attr_expected["levelup_points"])

@pytest.mark.parametrize('attr_expected', [
    {
        "xp_for_test": 11,
        "char_status": {"level": 2, "hp": 11, "attack": 2, "defense": 4},
        "class_special_attack": {"attack": 3, "heal": 0},
        "class_levelup_points": {"hp": 2, "attack": 3, "defense": 5}
    }
])
def test_player_levelUp(get_player, get_char_classes, attr_expected):
    player = get_player
    player.current_class = get_char_classes
    player.gain_xp(attr_expected["xp_for_test"])
    pClass = player.current_class

    # Char Status
    assert_attrs(player.char_status, attr_expected["char_status"])

    # Special attack
    assert_attrs(pClass.special_attack, attr_expected["class_special_attack"])

    # Levelup points
    assert_attrs(pClass.levelup_points, attr_expected["class_levelup_points"])
