from pyex2 import evaluate

def test_singleoperand():
    assert evaluate("6") == 6

def test_plus():
    assert evaluate("58+") == 13

def test_sub():
    assert evaluate("98-") == 1


