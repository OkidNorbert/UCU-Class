from vehicle import Vehicle 

class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer 
    
    def String(self):
        return super().String() + f"\nHas trailer: {self.has_trailer}"


# Example
# my_truck = Truck("RED")
# print(my_truck.String())