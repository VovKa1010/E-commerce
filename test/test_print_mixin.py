from src.product.product import Product
from src.product.smartphone import Smartphone
from src.product.lawn_grass import LawnGrass


def test_print_mixin(capsys):
    capsys.readouterr()

    Product("1", "1 description", 10, 15)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('1', '1 description', 10, 15)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('Газонная трава', 'Элитная трава для газона', 500.0, 20)"



