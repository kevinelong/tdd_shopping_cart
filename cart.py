from line_item import LineItem
from product import Product


class Cart:
    def __init__(self):
        self.line_items: [LineItem] = []

    def add_product(self, product: Product, quantity: int):
        self.line_items.append(LineItem(product, quantity))

    def get_total(self) -> int:
        total = 0
        for line in self.line_items:
            total += line.product.price * line.quantity

        return total

    def remove(self, line_item_number: int):
        self.line_items.remove(self.line_items[line_item_number - 1])

    def update_quantity(self, line_item_number: int, updated_quantity: int):
        self.line_items[line_item_number - 1].quantity = updated_quantity

    def __str__(self):
        output = []
        for line in self.line_items:
            output.append(f"{line.quantity} {line.product.name} {line.product.price} = {line.get_extended_price()}")
        output.append(f"total: {self.get_total()}")
        return "\n".join(output)
