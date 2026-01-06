import tkinter as tk
from tkinter import messagebox
from database import Database
from car import Car
import os

# Frisk database ved start (kan fjernes senere)
if os.path.exists("cars.db"):
    os.remove("cars.db")

db = Database("cars.db")

# ------------------------
# GUI HJÆLPEFUNKTIONER
# ------------------------

def show_result(text):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, text)

# ------------------------
# CREATE
# ------------------------

def create_car():
    window = tk.Toplevel(root)
    window.title("Opret bil")

    tk.Label(window, text="Mærke").pack()
    brand_entry = tk.Entry(window)
    brand_entry.pack()

    tk.Label(window, text="Model").pack()
    model_entry = tk.Entry(window)
    model_entry.pack()

    tk.Label(window, text="År").pack()
    year_entry = tk.Entry(window)
    year_entry.pack()

    def submit():
        try:
            car = db.create(
                brand_entry.get(),
                model_entry.get(),
                int(year_entry.get())
            )
            show_result(f"Oprettet:\n{car}")
            window.destroy()
        except ValueError:
            messagebox.showerror("Fejl", "År skal være et tal")

    tk.Button(window, text="Opret", command=submit).pack(pady=5)

# ------------------------
# READ (ENKELT)
# ------------------------

def read_car():
    window = tk.Toplevel(root)
    window.title("Find bil via ID")

    tk.Label(window, text="Bil ID").pack()
    id_entry = tk.Entry(window)
    id_entry.pack()

    def submit():
        car = db.read(int(id_entry.get()))
        if car:
            show_result(car)
        else:
            show_result("Bil ikke fundet")
        window.destroy()

    tk.Button(window, text="Find", command=submit).pack(pady=5)

# ------------------------
# READ ALL
# ------------------------

def read_all():
    cars = db.read_all()
    if not cars:
        show_result("Ingen biler i databasen")
        return

    text = ""
    for car in cars:
        text += str(car) + "\n" + "-"*30 + "\n"

    show_result(text)

# ------------------------
# UPDATE
# ------------------------

def update_car():
    window = tk.Toplevel(root)
    window.title("Opdater bil")

    tk.Label(window, text="Bil ID").pack()
    id_entry = tk.Entry(window)
    id_entry.pack()

    tk.Label(window, text="Nyt mærke").pack()
    brand_entry = tk.Entry(window)
    brand_entry.pack()

    tk.Label(window, text="Ny model").pack()
    model_entry = tk.Entry(window)
    model_entry.pack()

    tk.Label(window, text="Nyt år").pack()
    year_entry = tk.Entry(window)
    year_entry.pack()

    def submit():
        car = db.read(int(id_entry.get()))
        if not car:
            messagebox.showerror("Fejl", "Bil ikke fundet")
            return

        car.brand = brand_entry.get()
        car.model = model_entry.get()
        car.year = int(year_entry.get())

        success = db.update(car.id, car)
        if success:
            show_result(f"Opdateret:\n{car}")
        else:
            show_result("Opdatering fejlede")

        window.destroy()

    tk.Button(window, text="Opdater", command=submit).pack(pady=5)

# ------------------------
# DELETE
# ------------------------

def delete_car():
    window = tk.Toplevel(root)
    window.title("Slet bil")

    tk.Label(window, text="Bil ID").pack()
    id_entry = tk.Entry(window)
    id_entry.pack()

    def submit():
        success = db.delete(int(id_entry.get()))
        if success:
            show_result("Bil slettet")
        else:
            show_result("Bil ikke fundet")
        window.destroy()

    tk.Button(window, text="Slet", command=submit).pack(pady=5)

# ------------------------
# SEARCH
# ------------------------

def search_car():
    window = tk.Toplevel(root)
    window.title("Søg bil")

    tk.Label(window, text="Søgeord").pack()
    search_entry = tk.Entry(window)
    search_entry.pack()

    def submit():
        results = db.search(search_entry.get())
        if not results:
            show_result("Ingen resultater")
            return

        text = ""
        for car in results:
            text += str(car) + "\n" + "-"*30 + "\n"

        show_result(text)
        window.destroy()

    tk.Button(window, text="Søg", command=submit).pack(pady=5)

# ------------------------
# MAIN MENU
# ------------------------

root = tk.Tk()
root.title("Bil Database – CRUD")

tk.Label(root, text="CRUD Menu", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Opret bil (CREATE)", width=30, command=create_car).pack(pady=2)
tk.Button(root, text="Find bil (READ)", width=30, command=read_car).pack(pady=2)
tk.Button(root, text="Vis alle biler (READ ALL)", width=30, command=read_all).pack(pady=2)
tk.Button(root, text="Opdater bil (UPDATE)", width=30, command=update_car).pack(pady=2)
tk.Button(root, text="Slet bil (DELETE)", width=30, command=delete_car).pack(pady=2)
tk.Button(root, text="Søg bil (SEARCH)", width=30, command=search_car).pack(pady=2)

result_text = tk.Text(root, height=15, width=60)
result_text.pack(pady=10)

root.mainloop()
db.close()