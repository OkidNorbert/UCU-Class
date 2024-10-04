#OKIDI NORBERT B24281 S23B23/051 BSCS OOP ASSIGNMENT-1 ADVENT SEMSTER 2024

class Car:  
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def display_info(self):
        print(f"Car Information:\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nMileage: {self.mileage}")

    def drive(self, distance):
        self.mileage += distance


#   Creating three car objects
# car1 = Car("Toyota", "Corolla", 2020, 15000)
# car2 = Car("Honda", "Civic", 2018, 30000)
# car3 = Car("Ford", "Focus", 2019, 25000)

#  Displaying car information
# car1.display_info()
# car2.display_info()
# car3.display_info()

# Example of driving
car = Car("Toyota", "Corolla", 2020, 15000)
car.drive(100)
car.display_info()  # Mileage should now reflect 15100


class ElectricCar(Car):
    def __init__(self, brand, model, year, mileage, battery_capacity, charge_level):
        super().__init__(brand, model, year, mileage) 
        #super()._init_helps to invoke the _init_method of the car
        self.battery_capacity = battery_capacity
        self.charge_level = charge_level
    
    def charge(self, amount):
        self.charge_level = min(100, self.charge_level + amount) 
        # i used min() instead of a conditional statement like 'if (self.charge_level + amount) > 100' 
        # because it's more clean and simplier
    
    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh\nCharge Level: {self.charge_level}%")

# Example
toyota = ElectricCar("Toyota", "Corolla", 2020, 15000, 100, 50)
toyota.drive(100)
toyota.charge(30)
print("\nAfter driving 100 km....")
toyota.display_info()  # Charge should be updated to 80%

#                            Explanation for Task 3c:
#     Modularity: The ElectricCar class is a separate module that builds on Car, representing electric vehicles distinctly.
#     Reusability: The ElectricCar class reuses the attributes and methods from Car, saving code duplication.
#     Maintainability: Changes to car behavior can be managed in one place (the Car class), affecting all subclasses.


# Procedural programming version
def create_car(brand, model, year, mileage):
    return {"brand": brand, "model": model, "year": year, "mileage": mileage}

def display_info(car):
    print(f"\nCar Information:\nBrand: {car['brand']}\nModel: {car['model']}\nYear: {car['year']}\nMileage: {car['mileage']}")

def drive(car, distance):
    car["mileage"] += distance

# Using the procedural version
car = create_car("Toyota", "Corolla", 2020, 15000)
drive(car, 100)
display_info(car)


#                       Explanation for Task 4b:
# Differences:
    # In OOP, the Car class encapsulates both data (attributes) and behavior (methods), making it more organized.
    # Procedural programming separates data and functions, which can lead to less cohesion.

# Benefits of OOP:
    # Modularity: In OOP, each class can represent a module, isolating behavior and properties.
    # Reusability: OOP allows inheritance and polymorphism, making it easier to reuse code across different classes.
    # Maintainability: With encapsulation and abstraction, OOP systems are easier to maintain and 
                     # extend compared to procedural systems where functions are scattered.






#                ASSIGNMENT FROM THE SLIDES
class StudentManagement:
    def __init__(self):
        self.students = {}
        #i used a dictionary that stores student_id as the key and the student_name as the value

    def add_student(self, student_id, name):
        # Adds a new student to the system
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = name
        #stores data as   key   :   value
        print(f"Student {name} added with ID {student_id}.")

    def update_student(self, student_id, new_name):
        #Updates the name of an existing student
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        self.students[student_id] = new_name
        print(f"Student {student_id} updated to {new_name}.")

    def delete_student(self, student_id):
        #Deletes a student from the system
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        del self.students[student_id]
        print(f"Student {student_id} has been deleted.")

    #Extra method ('_') 
    def get_student(self, student_id):
        #Retrieves a student's details by their ID
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        return self.students[student_id]

# Example usage
print("\n**************Student Management:.******************************")
try:
    admin = StudentManagement()
    admin.add_student(1, "okidi norbert")
    admin.update_student(1, "Norbert Okidi")
    print(f"\n{admin.get_student(1)}")
    admin.delete_student(1)
    admin.get_student(1)  # This will raise an exception as the student no longer exists
except ValueError as e:
    print(f"Error: {e}")
                     