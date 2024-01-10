from ..player import Player
import pytest

@pytest.fixture
def create_player():
    print("Creating a dummy player")
    return Player(name="dummy_player_1")

@pytest.fixture
def create_player_without_name():
    print("Creating a dummy player without a Name")
    return Player()


def test_player_name_getter(create_player):
    assert create_player.name == "dummy_player_1"
    assert create_player.name == 'dummy_player_1'