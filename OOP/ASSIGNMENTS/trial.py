def create_car(brand, model, year, mileage):
    return {"brand": brand, "model": model, "year": year, "mileage": mileage}

def display_info(car):
    print(f"Car Information:\nBrand: {car['brand']}\nModel: {car['model']}\nYear: {car['year']}\nMileage: {car['mileage']}")

def drive(car, distance):
    car["mileage"] += distance

# Using the procedural version
car = create_car("Toyota", "Corolla", 2020, 15000)
drive(car, 100)
display_info(car)
