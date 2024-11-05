# Product Class
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def get_product_info(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}"

    def update_stock(self, quantity):
        self.stock -= quantity

# Customer Class
class Customer:
    def __init__(self, customer_id, name, email, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address

    def get_customer_info(self):
        return f"Customer: {self.name}, Email: {self.email}, Address: {self.address}"

# Cart Class
class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}  # Dictionary to hold products and their quantities

    def add_product(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
        product.update_stock(quantity)

    def remove_product(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def view_cart(self):
        cart_details = "************ DIDI **************\nCart Details:\n"
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            cart_details += f"{product.name} Quantity: {quantity} \n{product.name} Price: {product.price}\n"
        return cart_details

    def get_total(self):
        total = 0
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            total += product.price * quantity
        return total

# Order Class
class Order:
    order_count = 1  # Static variable to generate order IDs

    def __init__(self, customer, cart):
        self.order_id = Order.order_count
        Order.order_count += 1
        self.customer = customer
        self.cart = cart
        self.total_amount = cart.get_total()

    def place_order(self):
        return f"*****MY ORDER******\nOrder ID: {self.order_id}\nCustomer: {self.customer.name}\nTotal: {self.total_amount}"

# Payment Class
class Payment:
    payment_count = 1  # Static variable to generate payment IDs

    def __init__(self, order, amount):
        self.payment_id = Payment.payment_count
        Payment.payment_count += 1
        self.order = order
        self.amount = amount
        self.status = "Pending"

    def process_payment(self):
        if self.amount >= self.order.total_amount:
            self.status = "Success"
            self.comment = "\n *****THANKS FOR SHOPPING WITH US, COME AGAIN******"
        else:
            self.status = "Failed!"
            self.comment = "Amount is less, PLEASE ADD SOME CASH, DON'T BE STINGY"
        return f"Payment Status: {self.status}, Amount: {self.amount} \n{self.comment}"

# Creating products
product1 = Product(product_id=1, name="Laptop", price=1000, stock=5)
product2 = Product(product_id=2, name="Smartphone", price=500, stock=10)

# Creating a customer
customer1 = Customer(customer_id=1, name="Mustafa", email="mustafa@gmail.com", address="Buguju")

# Creating a shopping cart for the customer
cart = Cart(customer=customer1)

# Adding products to the cart
cart.add_product(product1, 2)  # Adding 2 laptops
cart.add_product(product2, 3)  # Adding 3 smartphones

# Viewing the cart
print(cart.view_cart())

# Creating an order
order = Order(customer=customer1, cart=cart)
print(order.place_order())

# Processing payment
payment = Payment(order=order, amount=3500)
print(payment.process_payment())


