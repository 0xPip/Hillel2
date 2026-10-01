class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        for item in self.items:
            if item["name"] == name:
                item["quantity"] = item["quantity"] + quantity
                item["price"] = price
                return
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return

    def get_total(self):
        total = 0
        for item in self.items:
            total = total + item["price"] * item["quantity"]
        return total