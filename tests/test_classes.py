import pytest

from src.classes import Category, Product


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
    assert smartphone_category.product_count == 2


def test_smartphone_category_products(smartphone_category):
    assert smartphone_category.products == "samsung, 17000.0 руб. Остаток 10 шт."
