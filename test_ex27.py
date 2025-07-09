# Logic
import pytest


# Not
def test_not():
    assert not False == True
    assert not True == False


# OR
def test_or():
    assert True or False == True
    assert True or True == True
    assert False or True == True
    assert False or False == False


# AND
def test_and_true_false():
    assert True and False == False

def test_and_true_true():
    assert True and True == True

def test_and_false_true():
    assert (False and True) == False

def test_and_false_false():
    assert (False and False) == False


# NOT OR
def test_not_true_false():
    assert not (True or False) == False

def test_not_true_true():
    assert not (True or True) == False

def test_not_false_true():
    assert not (False or True) == False

def test_not_false_false():
    assert not (False or False) == True


# NOT AND
def test_not_true_false():
    assert not (True and False) == True

def test_not_true_true():
    assert not (True and True) == False

def test_not_false_true():
    assert not (False and True) == True

def test_not_false_false():
    assert not (False and False) == True


# Not equal
def test_not_equal():
    assert (1 != 0) == True
    assert (1 != 1) == False
    assert (0 != 1) == True
    assert (0 != 0) == False

# Equal
def test_equal():
    assert (1 == 0) == False
    assert (1 == 1) == True
    assert (0 == 1) == False
    assert (0 == 0) == True
