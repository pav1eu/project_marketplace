import pytest

from src.classes import Category, Product


@pytest.fixture
def samsung_product():
    return Product("samsung", "it is cool", 17000.0, 10)


def test_samsung_product_init(samsung_product):
    assert samsung_product.name == "samsung"
    assert samsung_product.description == "it is cool"
    assert samsung_product.price == 17000.0
    assert samsung_product.quantity == 10


@pytest.fixture
def smartphone_category():
    return Category("samsung", "it is cool", ["samsung"])


def test_smartphone_category_init(smartphone_category):
    assert smartphone_category.name == "samsung"
    assert smartphone_category.description == "it is cool"
    assert len(smartphone_category.products) == 1
    assert smartphone_category.product_count == 1
    assert smartphone_category.category_count == 1
