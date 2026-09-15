from shopping_cart import ShoppingCart


class TestShoppingCart:
    def test_init_items_is_empty_list(self):
        cart = ShoppingCart()
        expected = []
        assert cart.items == expected

    def test_add_item_new_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        expected = [{"name": "apple", "price": 10, "quantity": 2}]
        assert cart.items == expected

    def test_add_item_several_new_items(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("banana", 5, 3)
        expected = [
            {"name": "apple", "price": 10, "quantity": 2},
            {"name": "banana", "price": 5, "quantity": 3},
        ]
        assert cart.items == expected

    def test_add_item_existing_item_sums_quantity(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("apple", 12, 3)
        expected = [{"name": "apple", "price": 12, "quantity": 5}]
        assert cart.items == expected

    def test_add_item_existing_item_overwrites_price(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("apple", 15, 1)
        expected_price = 15
        assert cart.items[0]["price"] == expected_price

    def test_remove_item_existing_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("banana", 5, 3)
        cart.remove_item("apple")
        expected = [{"name": "banana", "price": 5, "quantity": 3}]
        assert cart.items == expected

    def test_remove_item_nonexistent_item_does_nothing(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.remove_item("banana")
        expected = [{"name": "apple", "price": 10, "quantity": 2}]
        assert cart.items == expected

    def test_get_total_empty_cart(self):
        cart = ShoppingCart()
        expected = 0
        assert cart.get_total() == expected

    def test_get_total_single_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        expected = 20
        assert cart.get_total() == expected

    def test_get_total_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        cart.add_item("banana", 5, 3)
        expected = 35
        assert cart.get_total() == expected