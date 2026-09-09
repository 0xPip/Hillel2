import pytest

from password_checker import is_password_strong


@pytest.mark.parametrize("password, expected", [
    ("abc123!@", True),
    ("Qwerty1#", True),
    ("a1!bcdef", True),
    ("Zx9$mnop", True),
    ("short1!", False),
    ("nodigits!", False),
    ("12345678", False),
    ("!@#$%^&*", False),
    ("abc def1!", False),
    ("abc1234 ", False),
    ("", False),
    ("Ab1!", False),
])
def test_is_password_strong(password, expected):
    result = is_password_strong(password)
    assert result == expected


@pytest.mark.skip(reason="Test is not ready yet")
def test_password_variety_of_symbols():
    pass