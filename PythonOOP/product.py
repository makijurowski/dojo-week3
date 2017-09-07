"""This is a Coding Dojo homework assignment."""


class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'

    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, tax):
        self.tax = tax
        return (self.price * (1 + self.tax))

    def return_reason(self, reason):
        self.reason = reason
        if reason is 'defective':
            self.status = 'defective'
            self.price = 0
        elif self.status is 'like new':
            self.status = 'for sale'
        elif self.status is 'opened':
            self.status = 'used'
            self.price *= 0.8
        return self

    def display_info(self):
        print(
            'Item Name: ' + self.item_name + '\n'
            'Brand: ' + self.brand + '\n'
            'Weight: ' + self.weight + '\n'
            'Price: ' + self.price + '\n'
            'Status: ' + self.status + '\n'
        )
        return self
