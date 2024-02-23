from utils import sumar, restar

def test_sumar():
    assert sumar(2,4) == 6
    assert sumar(1,4) == 5
    assert sumar(2,2) == 4
    assert restar(2,4) == -2
    assert restar(4,4) == 0
    assert restar(4,2) == 2