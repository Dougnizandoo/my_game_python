import pytest
from app.models import EnumEnemy

@pytest.mark.parametrize('enum_enemy, hp, attack, defense', [
    (EnumEnemy.SLIME, 5, 1, 1),
    (EnumEnemy.GOBLIN, 7, 3, 4),
    (EnumEnemy.ZOMBIE, 10, 5, 3),
])
def test_enemy_creation_with_values(make_enemy, enum_enemy, hp, attack, defense):
    enemy = make_enemy(enum_enemy, hp, attack, defense)
    assert enemy.name == enum_enemy.name
    assert enemy.char_status.hp == hp
    assert enemy.char_status.attack == attack
    assert enemy.char_status.defense == defense
    assert enemy.enemy_type == enum_enemy


@pytest.mark.parametrize('enum_enemy, hp, attack, defense', [
    (EnumEnemy.SLIME, 10, 1, 1),
    (EnumEnemy.GOBLIN, 15, 3, 1),
    (EnumEnemy.ZOMBIE, 17, 4, 2),
    (None, 15, 3, 1)
])
def test_enemy_creation_with_default_values(make_enemy, enum_enemy, hp, attack, defense):
    if enum_enemy is None:
        enemy = make_enemy()
        assert enemy.name == EnumEnemy.GOBLIN.name
        assert enemy.enemy_type == EnumEnemy.GOBLIN
    else:
        enemy = make_enemy(enum_enemy, None, None, None)
        assert enemy.name == enum_enemy.name
        assert enemy.enemy_type == enum_enemy

    assert enemy.char_status.hp == hp
    assert enemy.char_status.attack == attack
    assert enemy.char_status.defense == defense
