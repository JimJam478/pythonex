from pyex2 import evaluate

def test_singleoperand():
    assert evaluate("6") == 6

def test_plus():
    assert evaluate("58+") == 13

def test_sub():
    assert evaluate("98-") == 1

def test_sub2():
    assert evaluate("36-") == -3

def test_prod():
    assert evaluate("37*") == 21

def test_div():
    assert evaluate("93/") == 3



