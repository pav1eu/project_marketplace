class Product:
    """Представляет имя продукта и его описание с ценой и количеством"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Представляет категорию продукта с описанием и списком продуктов,
    а так же ведет подсчёт количества категорий и продуктов
    """
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = list(products)

        Category.category_count += 1
        Category.product_count += len(products)
