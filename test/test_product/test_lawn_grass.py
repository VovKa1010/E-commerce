import pytest
from src.product.lawn_grass import LawnGrass
from test.test_product.test_product import product_1


@pytest.fixture()
def lawn_grass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый")


def test_lawn_grass_init(lawn_grass):
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_product_add_lawn_grass(lawn_grass):
    assert lawn_grass + lawn_grass == 20000


def test_product_add_smartphone_exception(lawn_grass):
    with pytest.raises(TypeError):
        lawn_grass + 0


def test_product_add_smartphone_with_product(lawn_grass, product_1):
    with pytest.raises(TypeError):
        lawn_grass + product_1
