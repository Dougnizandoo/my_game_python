import pytest


@pytest.mark.parametrize('status_alter, status_expected', [
    ((0, 0, 0, 0), (1, 10, 1, 2)),
    ((2, 5, 3, 5), (3, 15, 4, 7)),
    ((9, 90, 99, 98), (10, 100, 100, 100))
])
def test_player_status(get_player, status_alter, status_expected):
    player = get_player
    player.char_status.level += status_alter[0]
    player.char_status.hp += status_alter[1]
    player.char_status.attack += status_alter[2]
    player.char_status.defense += status_alter[3]

    assert player.char_status.level == status_expected[0]
    assert player.char_status.hp == status_expected[1]
    assert player.char_status.attack == status_expected[2]
    assert player.char_status.defense == status_expected[3]
