import pytest
from game_functions import enter_room

def test_enter_room():
    assert enter_room('main hall', 'outside') is 'main hall'
