import pytest
from products import Product


def test_valid_product():
    """Test that creating a normal product works."""
    p = Product("Laptop", price=1000, quantity=10)
    assert p.name == "Laptop"
    assert p.price == 1000
    assert p.quantity == 10
    assert p.is_active()


def test_invalid_product_name():
    """Test that creating a product with empty name raises ValueError."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_invalid_product_price():
    """Test that creating a product with negative price raises ValueError."""
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_prod_becomes_inactive():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    p = Product("iPhone12", price=500, quantity=1)
    p.set_quantity(0)
    assert not p.is_active()


def test_buy_modifies_quantity():
    """Test that product purchase modifies the quantity and returns the right total price."""
    p = Product("Apple AirPods 3", price=90, quantity=10)
    total_price = p.buy(2)
    assert total_price == 180
    assert p.get_quantity() == 8


def test_buy_too_much():
    """Test that buying more than available raises ValueError."""
    p = Product("Samsung Galaxy Tablet", price=300, quantity=5)
    with pytest.raises(ValueError):
        p.buy(10)
