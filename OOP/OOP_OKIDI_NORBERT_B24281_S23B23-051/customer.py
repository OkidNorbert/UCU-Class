class Customer:
    def __init__(self, name, address):
        self.name = name 
        self.address = address 

    def __str__(self): #I added this class beacuse without it, the output will not show the name or address
        return f"Name: {self.name}, Address: {self.address}"


# EXAMPLE
# customer = Customer("OKIDI NORBERT", "PDR HALL")
# print(customer)