#OKIDI NORBERT S23B23/051 B24281          BSCS OOP           TEST 2 QUESTION 1

class Character:
    def __init__(self, name, health, position):
        self.name = name
        self.health = health
        self.position = position
        self.current_vehicle = None  # Tracks the vehicle the character is in

    def move(self, new_position):
        """Moves the character to a new position."""
        self.position = new_position
        print(f"{self.name} moves to position {self.position}")

    def interact(self, vehicle):
        """Allows the character to interact with a vehicle."""
        print(f"{self.name} interacts with the {vehicle.type}")

    def attack(self, target):
        """Allows the character to attack another character."""
        print(f"{self.name} attacks {target.name}!")

    def get_in(self, vehicle):
        """Character gets into the vehicle."""
        if self.current_vehicle is None:
            self.current_vehicle = vehicle
            print(f"{self.name} gets into the {vehicle.type}")
        else:
            print(f"{self.name} is already in a vehicle.")

    def get_out(self):
        """Character gets out of the vehicle."""
        if self.current_vehicle:
            print(f"{self.name} gets out of the {self.current_vehicle.type}")
            self.current_vehicle = None
        else:
            print(f"{self.name} is not in any vehicle.")

    def drive_vehicle(self, distance):
        """Drives the vehicle the character is currently in."""
        if self.current_vehicle:
            self.current_vehicle.drive(distance)
        else:
            print(f"{self.name} is not in a vehicle to drive.")


# Specialized character class inheriting from Character
class HeroCharacter(Character):
    def __init__(self, name, health, position, special_ability):
        super().__init__(name, health, position)
        self.special_ability = special_ability

    def use_ability(self):
        """Uses the hero's special ability."""
        print(f"{self.name} uses their special ability: {self.special_ability}!")


# Vehicle class with drive, refuel, and stop methods
class Vehicle:
    def __init__(self, type, speed, fuel_level):
        self.type = type
        self.speed = speed
        self.fuel_level = fuel_level

    def drive(self, distance):
        """Drives the vehicle for a certain distance, consuming fuel."""
        fuel_needed = distance * 0.5
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"The {self.type} drives {distance} units")
        else:
            print(f"Not enough fuel to drive the {self.type}.")

    def refuel(self, amount):
        """Refuels the vehicle by a specified amount."""
        self.fuel_level += amount
        print(f"The {self.type} refueled by {amount} units. Total fuel: {self.fuel_level}")

    def stop(self):
        """Stops the vehicle."""
        print(f"The {self.type} has stopped")


# Enemy class, inheriting from Character, with unique attack behavior
class Enemy(Character):
    def __init__(self, name, health, position):
        super().__init__(name, health, position)

    def retaliate(self):
        """Enemy's counter-attack."""
        print(f"{self.name} retaliates fiercely!")


# Example scenario
def game():
    # Create the hero, enemy, and vehicle objects
    batman = HeroCharacter("Batman", 150, (0, 0), "Invisibility Cloak")
    joker = Enemy("Joker", 150, (10, 10))
    batmobile = Vehicle("Batmobile", speed=150, fuel_level=100)

    # Scenario starts
    print("\n---++++ Game Mission: Rescue Robin Hood Mission ++++---")
    print("Mission: Batman Needs to Rescue Robin Hood who has been captured by Joker.\n")

    # Step 1: Batman gets into the batmobile and drives closer to Joker's Home Turf
    batman.get_in(batmobile)
    batman.drive_vehicle(5)
    batmobile.stop()
    batman.get_out()


    # Step 2: Batman uses his special ability to approach unnoticed joker's lair
    batman.use_ability()
    batman.move((5, 5))

    
    # Step 3: Batman encounters the Joker and attacks
    batman.move((10, 10))
    batman.attack(joker)

    # Step 4: The Joker retaliates
    joker.retaliate()

    # Step 5: Batman uses his invisibility again to escape joker's defence moved to where Robin Hood is held and recused him
    batman.use_ability()
    batman.move((5,5))

    # Step 6: Batman uses the Batmobile to escape from Joker's Home Turf
    batman.interact(batmobile) #Batman calls the Batmobile
    batman.get_in(batmobile)
    batman.drive_vehicle(15)

    # Step 6: Batman returns safely with the Robin Hood
    batmobile.stop()
    batman.get_out()
    
    print(f"\nMission Complete: {batman.name} successfully retrieved Robin Hood and escaped!")
    print("\n---*********** End of Game ************---")


# Run the game scenario
game()

