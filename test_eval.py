from pyex2 import evaluate

def test_singleoperand():
    assert evaluate("6") == 6

def test_SingleOPER_OPND():
    assert not evaluate("5+") == 5

def test_plus():
    assert evaluate("58+") == 13

