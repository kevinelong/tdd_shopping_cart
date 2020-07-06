class LineItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_extended_price(self):
        return self.product.price * self.quantity
