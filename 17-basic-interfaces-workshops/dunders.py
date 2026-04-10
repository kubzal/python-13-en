class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.quantity} x {self.price} PLN)"

    def __float__(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product: Product):
        if product.name in self.items:
            self.items[product.name].quantity += product.quantity
        else:
            self.items[product.name] = product

    def __rshift__(self, product: Product):
        self.add_product(product)
        return self

    def __str__(self):
        return "\n".join(str(product) for product in self.items.values())

    def __float__(self):
        return sum(float(product) for product in self.items.values())

    def __len__(self):
        return sum(product.quantity for product in self.items.values())

# Example
cart1 = ShoppingCart()
cart1 >> Product(name = "Apple", price = 2.5, quantity = 4)
cart1 >> Product(name = "Banana", price = 3.0, quantity = 2)
cart1 >> Product(name = "Pear", price = 4.5, quantity = 1)

cart2 = ShoppingCart()
cart2 >> Product(name = "Orange", price = 5.0, quantity = 3)
cart2 >> Product(name = "Grapes", price = 10.0, quantity = 1)

# What is in the cart?
print("What is in the cart 1:")
print(cart1)
print(f"TOTAL value of the cart 1: {float(cart1)} PLN")
print(f"Number of products in the cart 1: {len(cart1)}")
print()

print("What is in the cart 2:")
print(cart2)
print(f"TOTAL value of the cart 2: {float(cart2)} PLN")
print(f"Number of products in the cart 2: {len(cart2)}")
print()

# # Compare two carts
# print(f"Is the cart 1 cheaper than the cart 2? {cart1 < cart2}")
# print(f"Is the cart 1 more expensive than cart 2? {cart1 > cart2}")
# print(f"Is the cart 1 the same value as the cart 2? {cart1 == cart2}")
#
# # Join carts
# cart3 = cart1 + cart2
# print(f"What is in the joined cart (cart 3):")
# print(cart3)
# print(f"TOTAL value of the cart 3: {float(cart3)} PLN")
# print()
#
# # Remove product from the cart
# item_to_remove = "Apple" # that might be input()
# cart1 << item_to_remove
# print(f"What is in the cart 1 after removing {item_to_remove}:")
# print(cart1)
# print()
#
# # Displaying the quantity of product in the cart
# item_to_check = "Banana" # that might be input()
# print(f"Number of {item_to_check} in the cart 1: {cart1[item_to_check]}")
# print()
#
# # Iteration through products inside any cart
# print("Iteration through products in the cart 3:")
# for product in cart3:
#     print(product)
#
#
# # Check if the product is inside the cart
# product_to_check = "Grapes"
# print(f"Do we have grapes in the cart 3? {product_to_check in cart3}")
#
# # Calling the cart
# cart3()
