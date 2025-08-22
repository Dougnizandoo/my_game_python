import pytest
from tests.models.helper import assert_attrs


@pytest.mark.parametrize("expected_attrs", [
    {
        "special_attack": {"name": "shield-breaker", "attack": 2, "heal": 0},
        "levelup_points": {"hp": 1, "attack": 1, "defense": 2}
    }
])
def test_char_classes_attributes(get_char_classes, expected_attrs):
    current_class = get_char_classes
    
    # Test special attack
    sa = current_class.special_attack
    assert_attrs(sa, expected_attrs["special_attack"])

    # Test levelup points
    lp = current_class.levelup_points
    assert_attrs(lp, expected_attrs["levelup_points"])

@pytest.mark.parametrize("expected_attrs", [
    {
        "new_level": 2,
        "special_attack": {"attack": 3, "heal": 0},
        "levelup_points": {"hp": 2, "attack": 3, "defense": 5}
    },
    {
        "new_level": 4,
        "special_attack": {"attack": 5, "heal": 0},
        "levelup_points": {"hp": 4, "attack": 7, "defense": 11}
    },
    {
        "new_level": 6,
        "special_attack": {"attack": 7, "heal": 2},
        "levelup_points": {"hp": 6, "attack": 11, "defense": 17}
    }
])
def test_char_classes_levelup(get_char_classes, expected_attrs):
    current_class = get_char_classes
    current_class.current_level = expected_attrs["new_level"]

    # test special attack
    sa = current_class.special_attack
    assert_attrs(sa, expected_attrs["special_attack"])

    # Test levelup points
    lup = current_class.levelup_points
    assert_attrs(lup, expected_attrs["levelup_points"])

