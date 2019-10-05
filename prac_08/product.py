""" My Product class

"""
class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = ""
        if self.is_on_sale:
            on_sale_string = " On Sale"
        return "Name: {} Price: ${:.2f}{}".format(self.name, self.price, on_sale_string)

