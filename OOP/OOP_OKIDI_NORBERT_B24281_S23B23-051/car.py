from vehicle import Vehicle 

class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires 
    
    def String(self):
        return super().String() + f"\nHas winter tires: {self.has_winter_tires}"


# Example
# my_car = Car("RED", "True")
# print(my_car.String())