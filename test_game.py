import pytest
from game_functions import standardise_text

def test_standardise_text():
    assert standardise_text("Main Hall") == "mainhall"
    assert standardise_text("MainHall") == "mainhall"
