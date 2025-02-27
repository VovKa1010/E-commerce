class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict, old_products: list = None):
        if old_products is None:
            return cls(**new_product)
        else:
            for old_product in old_products:
                if old_product["name"] == new_product["name"]:
                    new_product["quantity"] += old_product["quantity"]
                    if old_product["price"] > new_product["price"]:
                        new_product["price"] = old_product["price"]

            return cls(**new_product)


class Category:
    name: str
    description: str
    __products: [Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return result
