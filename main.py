from products import Product
from store import Store


# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


def start():
    """Display the menu"""
    print("   Store Menu    ")
    print("   __________")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. quit\n")


def show_products():
    """Display all active products in store."""
    print("______")
    for i, product in enumerate(best_buy.get_all_products()):
        print(f"{i + 1}. {product.show()}")
    print("_____\n")


def main():
    """Main function"""
    while True:
        # Display the menu
        start()

        # user input
        try:
            user_choice = input("Please choose a number (1-4): ")
            if user_choice not in ["1", "2", "3", "4"]:
                raise Exception
        except Exception:
            print("Invalid input! please enter a number between 1-4.\n")

        if user_choice == "1":
            show_products()

        if user_choice == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store\n")

        if user_choice == "3":
            show_products()

            print("When you want to finish order, enter empty text.")
            shopping_cart = []  # Store selected items here
            while True:
                product_choice = input("Which product # do you want? ")
                quantity_choice = input("What amount do you want? ")
                if product_choice == "" and quantity_choice == "":  # loop break while empty texts
                    print("********")
                    break

                try:
                    product_choice = int(product_choice)
                    quantity_choice = int(quantity_choice)
                    products = best_buy.get_all_products()
                    if 1 <= product_choice <= len(products):  # Only given product numbers
                        product = products[product_choice - 1]
                        shopping_cart.append((product, quantity_choice))
                        print("Product added to list!\n")
                    else:
                        print("Error adding! Invalid product number.")
                except ValueError:
                    print("Please enter valid numbers.")

            if shopping_cart:
                total_price = best_buy.order(shopping_cart)
                print(f"Order made! Total payment: ${total_price}\n")

        if user_choice == "4":
            break


if __name__ == "__main__":
    main()
