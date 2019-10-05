""" My Product class

"""
class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        return("Name: {} Price: {} Is_on_sale: {}".format(self.name, self.price, self.is_on_sale))

