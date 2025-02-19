import pytest

from src.classes import Category, Product
from src.subclasses import LawnGrass, Smartphone


@pytest.fixture
def samsung_product():
    return Product("samsung", "it is cool", 17000.0, 10)


@pytest.fixture
def xiaomi_product():
    return Product("xiaomi", "it is more cooler", 13000.0, 5)


def test_samsung_product_init(samsung_product):
    assert samsung_product.name == "samsung"
    assert samsung_product.description == "it is cool"
    assert samsung_product.price == 17000.0
    assert samsung_product.quantity == 10


def test_samsung_product_str(samsung_product, xiaomi_product):
    assert str(samsung_product) == "samsung, 17000.0 руб. Остаток 10 шт."


def test_samsung_product_add(samsung_product, xiaomi_product):
    assert samsung_product + xiaomi_product == 235000.0


def test_samsung_product_price(samsung_product):
    samsung_product.price = 0
    assert samsung_product.price == "Цена не должна быть нулевая или отрицательная"


@pytest.fixture
def smartphone_category(samsung_product):
    return Category(
        "Смартфоне", "Смартфоны, как средство не только коммуникации", [samsung_product]
    )


def test_smartphone_category_init(smartphone_category):
    assert smartphone_category.name == "Смартфоне"
    assert (
        smartphone_category.description
        == "Смартфоны, как средство не только коммуникации"
    )
    assert smartphone_category.product_count == 1
    assert smartphone_category.category_count == 1


def test_smartphone_category_str(smartphone_category):
    assert str(smartphone_category) == "Смартфоне, количество продуктов: 10 шт."


def test_smartphone_category_add_product(smartphone_category):
    new_product = Product("xiaomi", "it is more cooler", 13000.0, 5)
    smartphone_category.add_product(new_product)
    assert smartphone_category.product_count == 4


def test_smartphone_category_products(smartphone_category):
    assert smartphone_category.products == "samsung, 17000.0 руб. Остаток 10 шт."


@pytest.fixture
def samsung_product2():
    return Smartphone("samsung", "it is cool", 17000.0, 10, 25, "Mega", 11, "pink")


@pytest.fixture
def grass_product():
    return LawnGrass("grass", "very green grass", 150.0, 200, "USA", "5 sec", "yellow")


def test_invalid_sum(samsung_product2, grass_product):
    with pytest.raises(TypeError):
        samsung_product2 + grass_product


def test_add_product_not_product(smartphone_category):
    with pytest.raises(TypeError):
        smartphone_category.add_product("not a product")


def test_mixing_product():
    product1 = Product("not a product", "not a product", 10, 1)
    assert repr(product1) == "Product('not a product', 'not a product', 10, 1)"


def test_rises_quantity_init():
    with pytest.raises(ValueError):
        product1 = Product("not a product", "not a product", 10, 0)


def test_raises_category_middle_price():
    category1 = Category("not a category", "not a category", [])
    assert category1.middle_price() == 0
