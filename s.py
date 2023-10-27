class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items

class OrderPrinter:
    def print_order(self, order):
        pass