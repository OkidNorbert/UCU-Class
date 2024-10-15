class Vehicle:
    def __init__(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def String(self):
        return f"This vehicle is {self.color}"
    

    
#EXAMPLE
# my_vehicle = Vehicle("RED")
# print(my_vehicle.String())