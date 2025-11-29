class Car:
    def __init__(self, id, brand, model, year):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"Bil: {self.brand} {self.model}\nÅr: {self.year}"
