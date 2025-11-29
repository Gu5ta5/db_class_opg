import sqlite3
from car import Car

class Database:
    def __init__(self, db_name="cars.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self._create_table()
    
    def _create_table(self):
        """Opret tabel hvis den ikke eksisterer"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        """)
        self.conn.commit()
    
    def _run_query(self, query, params=()):
        """Kør SQL-query og returnér resultat som dict med 'rows'-nøgle"""
        self.cursor.execute(query, params)
        self.conn.commit()
        rows = [dict(row) for row in self.cursor.fetchall()]
        return {"rows": rows}
    
    def create(self, brand, model, year):
        """CREATE – Opret ny bil og returner Car-objekt"""
        self.cursor.execute(
            "INSERT INTO cars (brand, model, year) VALUES (?, ?, ?)",
            (brand, model, year)
        )
        self.conn.commit()
        car_id = self.cursor.lastrowid
        return Car(car_id, brand, model, year)
    
    def read(self, car_id):
        """READ – Hent bil efter id, returner Car-objekt eller None"""
        result = self._run_query(
            "SELECT id, brand, model, year FROM cars WHERE id = ?",
            (car_id,)
        )
        if result["rows"]:
            row = result["rows"][0]
            return Car(row["id"], row["brand"], row["model"], row["year"])
        return None
    
    def read_all(self):
        """READ_ALL – Hent alle biler, returner liste af Car-objekter"""
        result = self._run_query("SELECT id, brand, model, year FROM cars")
        return [Car(row["id"], row["brand"], row["model"], row["year"]) 
                for row in result["rows"]]
    
    def search(self, term):
        """SEARCH – Søg efter biler efter brand eller model"""
        result = self._run_query(
            "SELECT id, brand, model, year FROM cars WHERE brand LIKE ? OR model LIKE ?",
            (f"%{term}%", f"%{term}%")
        )
        return [Car(row["id"], row["brand"], row["model"], row["year"]) 
                for row in result["rows"]]
    
    def update(self, car_id, car):
        """UPDATE – Opdater en bil"""
        self.cursor.execute(
            "UPDATE cars SET brand = ?, model = ?, year = ? WHERE id = ?",
            (car.brand, car.model, car.year, car_id)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def delete(self, car_id):
        """DELETE – Slet en bil"""
        self.cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def close(self):
        """Luk databaseforbindelsen"""
        self.conn.close()
