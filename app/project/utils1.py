def calculate_discount(price: float, discount: float) -> float:
    """Повертає ціну після застосування знижки у відсотках."""
    return price - (price * discount / 100)


def is_even(number: int) -> bool:
    """Повертає True, якщо число парне, інакше False."""
    return number % 2 == 0


def get_full_name(first_name: str, last_name: str) -> str:
    """Повертає повне ім'я, зібране з імені та прізвища."""
    return f"{first_name} {last_name}"