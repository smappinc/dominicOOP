#Dominic Muhairwe M23B13/024
# https://github.com/smappinc/dominicOOP
class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
    
    def display_product_info(self):
        print(f"Product Name: {self.product_name}\n Price: UGX {self.price}\n Quantity in Stock: {self.quantity_in_stock}\n")
    

class ShoppingCart:
    total_carts = 0  # Class variable to track total number of shopping carts

    def __init__(self):
        self.items = []  # Instance variable for items in the cart
        ShoppingCart.total_carts += 1  # Increment the total carts count

    def add_to_cart(self, product, quantity):

        # Adding a product to the cart if the quantity is available.
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity  # Reduce the quantity in stock

            print(f"Added {quantity} of {product.product_name} to cart.\n")
        else:
            print(f"\nNot enough stock for {product.product_name}. Available: {product.quantity_in_stock}")

    def remove_from_cart(self, product):
        # Removes a product from the cart.
        for item in self.items:

            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]  # Restore the quantity in stock
                print(f"\nRemoved {product.product_name} from cart.")
                return
            
        print(f"\n{product.product_name} is not in the cart.")

    def display_cart(self):
        # Displays all items in the cart.
        print("\nShopping Cart:")
        for product, quantity in self.items:
            print(f"\n{product.product_name} - Quantity: {quantity}, Price: UGX {product.price}")

    def calculate_total(self):
        # Calculates and returns the total price of items in the cart.
        total = sum(product.price * quantity for product, quantity in self.items)
        return total


# Creating Product objects
laptop = Product("Laptop", 1500000, 5)
headphones = Product("Headphones", 250000, 10)
smartphone = Product("Smartphone", 3500000, 8)

# Display product info
laptop.display_product_info()
headphones.display_product_info()
smartphone.display_product_info()

# Creating two separate ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Adding products to cart1
cart1.add_to_cart(laptop, 1)
cart1.add_to_cart(headphones, 2)

# Adding products to cart2
cart2.add_to_cart(headphones, 1)
cart2.add_to_cart(smartphone, 3)

# Displaying contents of each cart
cart1.display_cart()
cart2.display_cart()

# Calculating and displaying the total amount due for each cart
total_cart1 = cart1.calculate_total()
total_cart2 = cart2.calculate_total()

print(f"\nTotal amount due for Cart 1: UGX {total_cart1}")
print(f"\nTotal amount due for Cart 2: UGX {total_cart2}")

# Removing an item from cart1
cart1.remove_from_cart(headphones)
cart2.remove_from_cart(headphones)

# Displaying cart after removal
cart1.display_cart()
print(f"\nTotal amount due for Cart 1 after removal: UGX {cart1.calculate_total()}")

cart2.display_cart()
print(f"\nTotal amount due for Cart 1 after removal: UGX {cart2.calculate_total()}")