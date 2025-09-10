class Product:

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        if not name:
            raise ValueError("Invalid input, name is required!")
        self.price = price
        if price < 0:
            raise ValueError("Invalid input, price must be greater than or equal to 0!")
        self.quantity = quantity
        if quantity < 0:
            raise ValueError("Invalid input, quantity must be greater than or equal to 0!")
        self.active = True

    def get_quantity(self):
        """Return the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Update the quantity of the product.
        if it reaches 0, the product will be deactivated."""
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
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
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int):
        """Buy quantity of the product and return the total price."""
        if quantity <= 0:
            raise ValueError("Invalid input, quantity must be greater than 0!")
        if quantity > self.quantity:
            raise ValueError("There are less than the product quantity!")
        if not self.active:
            raise ValueError("Product is not available!")
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return float(total_price)


