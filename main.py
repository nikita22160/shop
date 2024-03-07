class Category:
    """Класс для представления категории."""
    all_quantity_category = 0
    all_quantity_unique_product = 0
    name: str
    description: str
    product: list

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        self.all_quantity_category = 1

        Category.all_quantity_unique_product += 1


class Product:
    """Класс для продуктов."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity
