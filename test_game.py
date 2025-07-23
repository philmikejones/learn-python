import pytest
from game_rooms import rooms
from game_functions import standardise_text
from game_functions import enter_room

def test_standardise_text():
    assert standardise_text("Main Hall") == "mainhall"
    assert standardise_text("MainHall") == "mainhall"
    with pytest.raises(Exception):
        standardise_text(int(1))

def test_enter_room():
    # Can get to main hall from outside
    assert enter_room("outside", "main hall") == "mainhall"
    # Cannot get to dining room from outside
    assert enter_room("outside", "dining room") == "outside"
