from utils import is_nuber_positive

def test_is_nuber_positive():
    number = 1
    expected = True
    actual = is_nuber_positive(number)
    assert expected is actual

def test_is_nuber_positive_1():
    number = -5
    expected = True
    actual = is_nuber_positive(number)
    assert expected is actual


def test_is_nuber_positive():
    number = 5
    expected = True
    actual = is_nuber_positive(number)
    assert expected is actual
