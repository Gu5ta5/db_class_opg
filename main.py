from database import Database
from car import Car

# Slet gamle database for frisk start
import os
if os.path.exists("cars.db"):
    os.remove("cars.db")

# Opret database-instans
db = Database("cars.db")

print("=== OPRETTELSE (CREATE) ===")
car1 = db.create("Toyota", "Corolla", 2020)
print(f"Oprettet: {car1.brand} {car1.model} (id={car1.id})")

car2 = db.create("Volvo", "XC90", 2022)
print(f"Oprettet: {car2.brand} {car2.model} (id={car2.id})")

car3 = db.create("BMW", "X3", 2021)
print(f"Oprettet: {car3.brand} {car3.model} (id={car3.id})")

print("\n=== VIS ALLE (READ_ALL) ===")
all_cars = db.read_all()
for car in all_cars:
    print(car)
    print("---")

print("\n=== HEN ENKELT (READ) ===")
car = db.read(1)
if car:
    print(car)
else:
    print("Bil ikke fundet")

print("\n=== SØGNING (SEARCH) ===")
search_results = db.search("Volvo")
print(f"Søgte efter 'Volvo', fandt {len(search_results)} resultat(er):")
for car in search_results:
    print(car)
    print("---")

print("\n=== OPDATERING (UPDATE) ===")
car_to_update = db.read(2)
if car_to_update:
    car_to_update.year = 2023
    success = db.update(2, car_to_update)
    print(f"Opdatering {'lykkedes' if success else 'fejlede'}")
    updated_car = db.read(2)
    print("Opdateret bil:")
    print(updated_car)

print("\n=== SLETNING (DELETE) ===")
success = db.delete(3)
print(f"Sletning af id=3 {'lykkedes' if success else 'fejlede'}")

print("\n=== VIS ALLE EFTER SLETNING ===")
all_cars = db.read_all()
print(f"Antal biler tilbage: {len(all_cars)}")
for car in all_cars:
    print(car)
    print("---")

db.close()
print("\n✅ Alle operationer afsluttet!")
