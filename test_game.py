import pytest
from game_rooms import all_rooms
from game_functions import standardise_text
from game_functions import enter_room
from game_functions import inventory_full
from game_functions import inventory_add
from game_functions import remove_room_item

def test_remove_room_item():
    dining_room_items = remove_room_item(item_taken = 'emblem', current_room = 'diningroom')
    assert dining_room_items == []

def test_inventory_add():
    test_inventory = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    test = inventory_add('another_item', test_inventory)
    assert len(test) == 8
    test_inventory = []
    test = inventory_add('another_item', test_inventory)
    assert len(test) == 1
    assert test == ['another_item']

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

def test_inventory_full():
    test_inventory = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    assert inventory_full(inventory = test_inventory)
    test_inventory = ['a']
    assert not inventory_full(inventory = test_inventory)
    with pytest.raises(TypeError):
        inventory_full(inventory = 'not a list')
