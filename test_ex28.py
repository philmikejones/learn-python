import pytest

def test_logic():
    assert (True and True) == True
    assert (False and True) == False
    assert (1 == 1 and 2 == 1) == False  # True and False
    assert ('test' == 'test') == True
    assert (1 == 1 or 2 != 1) == True    # True or True
    assert (True and 1 == 1) == True     # True and True
    assert (False and 0 != 0) == False   # False and False
    assert (True or 1 == 1) == True  # True or True
    assert ('test' == 'testing') == False
    assert ('test' == 1) == False
    assert not (True and False) == True
    assert not (1 == 1 and 0 != 1) == False  # True and True
    assert not (10 == 1 or 1000 == 1000) == False  # False or True
    assert not (1 != 10 or 3 == 4) == False  # True or False
    assert not ('testing' == 'testing' and 'Zed' == 'author') == True  # True and False
    assert 1 == 1 and (not ('testing' == 1 or 1 == 0)) == True  # True and (not(False or False))
    assert ('chunky' == 'bacon' and (not (3 == 4 or 3 == 3))) == False  # False and (not (False or True))
    assert 3 == 3 and (not ("testing" == "testing" or 'python' == 'fun')) == False  # True and not (True or False)
