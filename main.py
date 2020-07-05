"""
REQUIREMENTS:
Create a traditional shopping cart where items can be added,
with a quantity, and having a price each.
Display all items in cart including their descriptions,
quantities and extended price. Plus a grand total.

Entities (Nouns):
Cart
Item

Methods (Verbs):
add_item
remove_item
update_quantity
display_cart

Properties (Adverbs and Adjectives):
item_price
item_quantity
extended_price
grand_total

Use Case:
As a user I want to add items to a cart, so I can review them,
and revise them.
"""


class LineItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def get_extended_price(self):
        return self.item.price * self.quantity


class Cart:
    def __init__(self):
        self.line_items = []

    def add_item(self, item, quantity):
        self.line_items.append(LineItem(item, quantity))

    def get_total(self):
        total = 0
        for line in self.line_items:
            total += line.item.price * line.quantity

        return total

    def remove(self, line_item_number):
        self.line_items.remove(self.line_items[line_item_number - 1])

    def update_quantity(self, line_item_number, updated_quantity):
        self.line_items[line_item_number - 1].quantity = updated_quantity

    def __str__(self):
        output = []
        for line in self.line_items:
            output.append(f"{line.quantity} {line.item.name} {line.item.price} = {line.get_extended_price()}")
        output.append(f"total: {self.get_total()}")
        return "\n".join(output)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Not everything is a class!
def display_cart(cart):
    print(f"CART:\n{cart}\n")


# TESTS - ALL PASSING then REFACTOR

c = Cart()
item = Item("widget", 123)
c.add_item(item, 100)
item2 = Item("gadget", 45)
c.add_item(item2, 1)
assert c.get_total() == 12345  # 100x123=12300 + 1x45=45
assert len(c.line_items) == 2
assert c.line_items[0].get_extended_price() == 12300
assert c.line_items[1].get_extended_price() == 45
content = str(c)
assert content.find("widget") != -1
assert content.find("gadget") != -1
assert content.find("123") != -1
assert content.find("12300") != -1
assert content.find("1") != -1
assert content.find("45") != -1
assert content.find("total") != -1
assert content.find("12345") != -1
display_cart(c)

c.remove(2)
c.update_quantity(1, 200)  # line number and quantity
content = str(c)
assert content.find("24600") != -1  # 123x200=24600

display_cart(c)
