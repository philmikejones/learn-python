import pytest
import game_ex36.py as game

def test_enter_room():
    assert game.enter_room('main hall', 'outside') is 'main hall'
