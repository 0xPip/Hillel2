import pytest

from shoppingcart import ShoppingCart

@pytest.fixture
def default_item():
    return {"name": "apple", "price": 10, "quantity": 2}


@pytest.fixture
def cart_with_default_item(default_item):
    cart = ShoppingCart()
    cart.add_item(default_item["name"], default_item["price"], default_item["quantity"])
    return cart


class TestShoppingCart:
    def test_init_items_is_empty_list(self):
        cart = ShoppingCart()
        expected = []
        assert cart.items == expected

    def test_add_item_new_item(self, default_item):
        cart = ShoppingCart()
        cart.add_item(default_item["name"], default_item["price"], default_item["quantity"])
        expected = [default_item]
        assert cart.items == expected

    def test_add_item_several_new_items(self, cart_with_default_item):
        cart_with_default_item.add_item("banana", 5, 3)
        expected = [
            {"name": "apple", "price": 10, "quantity": 2},
            {"name": "banana", "price": 5, "quantity": 3},
        ]
        assert cart_with_default_item.items == expected

    def test_add_item_existing_item_sums_quantity(self, cart_with_default_item):
        cart_with_default_item.add_item("apple", 12, 3)
        expected = [{"name": "apple", "price": 12, "quantity": 5}]
        assert cart_with_default_item.items == expected

    def test_add_item_existing_item_overwrites_price(self, cart_with_default_item):
        cart_with_default_item.add_item("apple", 15, 1)
        expected_price = 15
        assert cart_with_default_item.items[0]["price"] == expected_price

    def test_remove_item_existing_item(self, cart_with_default_item):
        cart_with_default_item.add_item("banana", 5, 3)
        cart_with_default_item.remove_item("apple")
        expected = [{"name": "banana", "price": 5, "quantity": 3}]
        assert cart_with_default_item.items == expected

    def test_remove_item_nonexistent_item_does_nothing(self, cart_with_default_item, default_item):
        cart_with_default_item.remove_item("banana")
        expected = [default_item]
        assert cart_with_default_item.items == expected

    def test_get_total_empty_cart(self):
        cart = ShoppingCart()
        expected = 0
        assert cart.get_total() == expected

    def test_get_total_single_item(self, cart_with_default_item):
        expected = 20
        assert cart_with_default_item.get_total() == expected

    def test_get_total_multiple_items(self, cart_with_default_item):
        cart_with_default_item.add_item("banana", 5, 3)
        expected = 35
        assert cart_with_default_item.get_total() == expected