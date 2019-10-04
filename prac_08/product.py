""" My Product class

"""
class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        print("Running init")
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

