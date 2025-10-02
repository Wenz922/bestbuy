from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """Apply promotion and return total price."""
        pass

    def __str__(self):
        return self.name


class PercentDiscount(Promotion):
    """Percentage discount (e.g. 20% off)."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount = (self.percent / 100)
        return product.price * quantity * (1 - discount)


class SecondHalfPrice(Promotion):
    """Second item at half price."""

    def apply_promotion(self, product, quantity) -> float:
        pairs = quantity // 2
        remainder = quantity % 2
        return pairs * (product.price + product.price * 0.5) + remainder * product.price


class ThirdOneFree(Promotion):
    """Buy 2, get 1 free."""

    def apply_promotion(self, product, quantity) -> float:
        groups_of_three = quantity // 3
        remainder = quantity % 3
        return groups_of_three * (2 * product.price) + remainder * product.price
