# TESTS - ALL PASSING then REFACTOR
from cart import Cart
from product import Product


# Helper
def display_cart(cart: Cart) -> object:
    print(f"CART:\n{cart}\n")


def test_cart():
    c = Cart()
    p = Product("widget", 123)
    c.add_product(p, 100)
    item2 = Product("gadget", 45)
    c.add_product(item2, 1)
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


if __name__ == "__main__":
    test_cart()
