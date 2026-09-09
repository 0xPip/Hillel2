from utils1 import calculate_discount, is_even, get_full_name


# Тести для calculate_discount

def test_calculate_discount_1():
    price = 100
    discount = 20
    expected = 80
    assert calculate_discount(price, discount) == expected


def test_calculate_discount_2():
    price = 200
    discount = 50
    expected = 100
    assert calculate_discount(price, discount) == expected


def test_calculate_discount_3():
    price = 150
    discount = 0
    expected = 150
    assert calculate_discount(price, discount) == expected


def test_calculate_discount_4():
    price = 0
    discount = 30
    expected = 0
    assert calculate_discount(price, discount) == expected


def test_calculate_discount_5():
    price = 500
    discount = 100
    expected = 0
    assert calculate_discount(price, discount) == expected


# Тести для is_even

def test_is_even_1():
    number = 4
    expected = True
    assert is_even(number) == expected


def test_is_even_2():
    number = 7
    expected = False
    assert is_even(number) == expected


def test_is_even_3():
    number = -8
    expected = True
    assert is_even(number) == expected


def test_is_even_4():
    number = -3
    expected = False
    assert is_even(number) == expected


def test_is_even_5():
    number = 0
    expected = True
    assert is_even(number) == expected


# Тести для get_full_name

def test_get_full_name_1():
    first_name = "Artem"
    last_name = "Polishchuk"
    expected = "Artem Polishchuk"
    assert get_full_name(first_name, last_name) == expected


def test_get_full_name_2():
    first_name = "Bro"
    last_name = "Ok"
    expected = "Bro Ok"
    assert get_full_name(first_name, last_name) == expected


def test_get_full_name_3():
    first_name = "Topolya"
    last_name = "Topolski"
    expected = "Topolya Topolski"
    assert get_full_name(first_name, last_name) == expected


def test_get_full_name_4():
    first_name = "A"
    last_name = "B"
    expected = "A B"
    assert get_full_name(first_name, last_name) == expected


def test_get_full_name_5():
    first_name = "Sasha"
    last_name = "Nikitenko"
    expected = "Sasha Nikitenko"
    assert get_full_name(first_name, last_name) == expected