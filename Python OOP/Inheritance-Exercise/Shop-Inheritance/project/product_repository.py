from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []  # containing all the products(objects)

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product_name == product.name:
                return product

    def remove(self, product_name: str):
        for product in self.products:
            if product_name == product.name:
                self.products.remove(product)

    def __repr__(self):
        info = ""
        for product in self.products:
            info += f"{product.name}: {product.quantity}\n"
        return info
