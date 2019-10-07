"""
Testing my Product class
"""

from product import Product

products = [Product("Bee Hive", 200, False), Product("Car", 5000, True), Product("Pick", 50, True)]
on_sale_products = [Product for product in products if product.is_on_sale]
print(on_sale_products)
