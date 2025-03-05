import pytest
from src.product.smartphone import Smartphone
from test.test_product.test_product import product_1


@pytest.fixture()
def smartphone():
    return Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space")


def test_smartphone_init(smartphone):
    assert smartphone.name == "Iphone 15"
    assert smartphone.description == "512GB, Gray space"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray space"


def test_product_add_smartphone(smartphone):
    assert smartphone + smartphone == 3360000


def test_product_add_smartphone_exception(smartphone):
    with pytest.raises(TypeError):
        smartphone + 0


def test_product_add_smartphone_with_product(smartphone, product_1):
    with pytest.raises(TypeError):
        smartphone + product_1
