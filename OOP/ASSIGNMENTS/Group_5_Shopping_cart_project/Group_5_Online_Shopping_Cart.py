# Product Class
class Product:
    """Represents a product with ID, name, price, and stock availability."""

    def __init__(self, product_id, name, price, stock):
        # Encapsulated product attributes
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def get_product_info(self):
        """Returns a string with product information."""
        return f"Product: {self._name}, Price: {self._price}, Stock: {self._stock}"

    def update_stock(self, quantity):
        """Updates the stock by reducing it by the quantity sold."""
        if quantity <= self._stock:
            self._stock -= quantity
        else:
            print("Not enough stock available")

    @property
    def price(self):
        """Returns the price of the product."""
        return self._price

    @property
    def name(self):
        """Returns the name of the product."""
        return self._name

# Function to display all products in the catalog
def display_product_catalog(products):
    """Displays information for all products in the product catalog."""
    catalog = "**** Product Catalog ****\n"
    for product in products:
        catalog += product.get_product_info() + "\n"
    return catalog

# Customer Class
class Customer:
    """Represents a customer with ID, name, email, and address."""

    def __init__(self, customer_id, name, email, address):
        # Encapsulated customer attributes
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._address = address

    def get_customer_info(self):
        """Returns a string with customer information."""
        return f"Customer ID: {self._customer_id}, Name: {self._name}, Email: {self._email}, Address: {self._address}"

# Cart Class
class Cart:
    """Represents a shopping cart containing multiple products and their quantities."""

    def __init__(self, customer):
        # Encapsulated attributes for customer and cart items
        self._customer = customer
        self._items = {}

    def add_product(self, product, quantity):
        """Adds a product to the cart with a specified quantity."""
        if product._product_id in self._items:
            self._items[product._product_id]['quantity'] += quantity
        else:
            self._items[product._product_id] = {'product': product, 'quantity': quantity}
        product.update_stock(quantity)

    def remove_product(self, product_id):
        """Removes a product from the cart by product ID."""
        if product_id in self._items:
            del self._items[product_id]

    def view_cart(self):
        """Displays the details of all products in the cart."""
        cart_details = "************ CART DETAILS **************\n"
        for item in self._items.values():
            product = item['product']
            quantity = item['quantity']
            cart_details += f"{product.name} - Quantity: {quantity} - Price: {product.price}\n"
        return cart_details

    def get_total(self):
        """Calculates and returns the total cost of the products in the cart."""
        total = 0
        for item in self._items.values():
            product = item['product']
            quantity = item['quantity']
            total += product.price * quantity
        return total

    def checkout_summary(self):
        """Provides a summary of the cart with the total cost."""
        summary = self.view_cart()
        total = self.get_total()
        summary += f"Total Cost: {total}\n"
        return summary

# Order Class
class Order:
    """Represents an order placed by a customer."""

    # Static variable to keep track of order count and assign unique order IDs
    order_count = 1

    def __init__(self, customer, cart):
        # Encapsulated attributes for order details
        self._order_id = Order.order_count
        Order.order_count += 1
        self._customer = customer
        self._cart = cart
        self._total_amount = cart.get_total()

    def place_order(self):
        """Returns a string with the order details."""
        return f"***** ORDER DETAILS *****\nOrder ID: {self._order_id}\n{self._customer.get_customer_info()}\nTotal Amount: {self._total_amount}"

# Base Payment Class
class Payment:
    """Base class representing a generic payment process."""

    # Static variable to keep track of payment count and assign unique payment IDs
    payment_count = 1

    def __init__(self, order, amount):
        # Encapsulated attributes for payment details
        self._payment_id = Payment.payment_count
        Payment.payment_count += 1
        self._order = order
        self._amount = amount
        self._status = "Pending"

    def process_payment(self):
        """A method meant to be overridden in subclasses to process payment."""
        raise NotImplementedError("Subclasses should implement this method")

# CreditCardPayment Class
class CreditCardPayment(Payment):
    """Represents payment processing through credit card."""

    def process_payment(self):
        """Processes payment and checks if the amount meets the order's total."""
        if self._amount >= self._order._total_amount:
            self._status = "Success"
            self._comment = "***** THANK YOU FOR SHOPPING WITH US *****"
        else:
            self._status = "Failed"
            self._comment = "Insufficient funds. Please add more money."
        return f"Payment Status: {self._status}, Amount: {self._amount}\n{self._comment}"

# PayPalPayment Class
class PayPalPayment(Payment):
    """Represents payment processing through PayPal."""

    def process_payment(self):
        """Processes payment and checks if the amount meets the order's total."""
        if self._amount >= self._order._total_amount:
            self._status = "Success"
            self._comment = "***** PAYMENT COMPLETED VIA PAYPAL *****"
        else:
            self._status = "Failed"
            self._comment = "PayPal payment failed. Insufficient funds."
        return f"Payment Status: {self._status}, Amount: {self._amount}\n{self._comment}"

# Example Usage
# Step 1: Product Catalog
product1 = Product(product_id=1, name="Laptop", price=1000, stock=5)
product2 = Product(product_id=2, name="Smartphone", price=500, stock=10)
product3 = Product(product_id=3, name="Tablet", price=300, stock=15)
product4 = Product(product_id=4, name="Headphones", price=150, stock=20)
product5 = Product(product_id=5, name="Smartwatch", price=200, stock=8)
product6 = Product(product_id=6, name="Camera", price=1200, stock=6)

# Adding all products to the catalog list
products = [product1, product2, product3, product4, product5, product6]

# Displaying the product catalog
print(display_product_catalog(products))

# Step 2: Create a customer
customer1 = Customer(customer_id=1, name="Mustafa", email="mustafa@gmail.com", address="Buguju")

# Step 3: Create a shopping cart for the customer
cart = Cart(customer=customer1)

# Step 4: Add products to the cart
cart.add_product(product1, 2)  # Adding 2 laptops
cart.add_product(product2, 3)  # Adding 3 smartphones

# Step 5: View the cart and checkout
print(cart.view_cart())
print(cart.checkout_summary())

# Step 6: Create an order
order = Order(customer=customer1, cart=cart)
print(order.place_order())

# Step 7: Process payment using polymorphism
payment1 = CreditCardPayment(order=order, amount=3500)
print(payment1.process_payment())

payment2 = PayPalPayment(order=order, amount=3000)
print(payment2.process_payment())

