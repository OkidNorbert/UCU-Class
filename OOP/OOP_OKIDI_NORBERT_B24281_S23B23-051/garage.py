from car import Car
from truck import Truck

class Garage:
    def __init__(self):
        self.parked_vehicle = None 
    
    def setVehicle(self, vehicle):
        self.parked_vehicle = vehicle 
    
    def String(self):
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle}"
        else:
            return "No vehicle is parked in the garage."

# Example
# car = Car("blue","True")
# truck = Truck("black")
# garage = Garage()

# garage.setVehicle(car)
# print(garage.String(), car.String())

# garage.setVehicle(truck)
# print(garage.String(), truck.String())