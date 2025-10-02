class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Invalid input, name is required!")
        if price < 0:
            raise ValueError("Invalid input, price must be greater than or equal to 0!")
        if quantity < 0:
            raise ValueError("Invalid input, quantity must be greater than or equal to 0!")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Update the quantity of the product.
        if it reaches 0, the product will be deactivated."""
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Display the product information."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """Buy quantity of the product and return the total price."""
        if quantity <= 0:
            raise ValueError("Invalid input, quantity must be greater than 0!")
        if quantity > self.quantity:
            raise ValueError("Error while making order! Quantity larger than what exists.")
        if not self.active:
            raise ValueError("Product is not available!")
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price


# Non-stocked product
class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Non-stocked products always have 0 quantity and stay this way."""
        self.quantity = 0

    def buy(self, quantity: int) -> float:
        """Buy quantity of the product and return the total price, quantity doesn't change."""
        if quantity <= 0:
            raise ValueError("Quantity must be > 0!")
        # no stock to reduce, just charge
        return quantity * self.price

    def show(self):
        """Display the product information."""
        return f"{self.name} (Non-stocked), Price: {self.price}"


# Limited product
class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """Buy quantity of the product and return the total price, can't buy given maximum quantity."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of {self.name} in one order!")
        return super().buy(quantity)

    def show(self):
        """Display the product information."""
        return f"{self.name} (Limited, max {self.maximum} per order), Price: {self.price}, Quantity: {self.quantity}"
