import pytest

from src.subclasses import LawnGrass, Smartphone


@pytest.fixture
def samsung_product():
    return Smartphone("samsung", "it is cool", 17000.0, 10, 25, "Mega", 11, "pink")


@pytest.fixture
def grass_product():
    return LawnGrass("grass", "very green grass", 150.0, 200, "USA", "5 sec", "yellow")


def test_smartphone_init(samsung_product):
    assert samsung_product.name == "samsung"
    assert samsung_product.description == "it is cool"
    assert samsung_product.price == 17000.0
    assert samsung_product.quantity == 10
    assert samsung_product.efficiency == 25
    assert samsung_product.model == "Mega"
    assert samsung_product.memory == 11
    assert samsung_product.color == "pink"


def test_grass_init(grass_product):
    assert grass_product.name == "grass"
    assert grass_product.description == "very green grass"
    assert grass_product.price == 150.0
    assert grass_product.quantity == 200
    assert grass_product.country == "USA"
    assert grass_product.germination_period == "5 sec"
    assert grass_product.color == "yellow"
