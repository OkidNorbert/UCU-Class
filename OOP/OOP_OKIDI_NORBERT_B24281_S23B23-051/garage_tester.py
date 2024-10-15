from truck import Truck 
from garage import Garage   


class GarageTester:
    def getExample(self):
        truck = Truck(color="black", has_trailer=False)
        
        garage = Garage()
        garage.setVehicle(truck)
        print(garage.String())



# if __name__ == "__main__":
#     tester = GarageTester()
#     tester.getExample()


