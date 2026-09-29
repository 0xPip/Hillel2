import pytest
from shopping_cart import ShoppingCart


@pytest.fixture
def default_product():
    return {"name": "apple", "price": 10, "quantity": 2}


@pytest.fixture
def cart_with_default_product(default_product):
    cart = ShoppingCart()
    cart.add_item(default_product["name"], default_product["price"], default_product["quantity"])
    return cart