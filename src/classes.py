from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


class MixinLog:
    """Миксин для добавления методов логирования с продуктами"""

    def __init__(self):
        self.__repr__()
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Product(MixinLog, BaseProduct):
    """Представляет имя продукта и его описание с ценой и количеством"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток {self.quantity} шт."

    def __add__(self, other):
        if type(other) is type(self):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @classmethod
    def new_product(cls, new_product: dict):
        """Возвращает созданный объект класса Product из параметров товара в словаре"""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            self.__price = "Цена не должна быть нулевая или отрицательная"
        else:
            self.__price = price


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
        self.__products = list(products)

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f"{self.name}, количество продуктов: {total_products} шт."

    def add_product(self, products):
        if isinstance(products, Category):
            self.__products.append(products)
            Category.product_count += 1
        elif issubclass(products.__class__, Product):
            self.__products.append(products)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return "; ".join([str(product) for product in self.__products])

    def middle_price(self) -> float:
        """Метод для подсчёта среднего ценника товара."""
        total = sum(product.price * product.quantity for product in self.__products)
        try:
            avg = total / len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return round(avg, 2)
