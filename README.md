# OOP Database Assignment (Programmering B)

## Opgave: DB + Entitet (Biler)

Denne løsning implementerer en database-klasse, der arbejder med Car-objekter i SQLite.

### Filer

- **`car.py`** – Entitet-klasse `Car` med `__str__()`-metode
- **`database.py`** – Database-klasse med CRUD-operationer, returnerer `Car`-objekter
- **`main.py`** – Demo-script som viser alle operationer

### Funktionalitet

Database-klassen implementerer alle CRUD-operationer:

1. **CREATE** – Opret ny bil: `db.create(brand, model, year)` → returnerer `Car`-objekt
2. **READ** – Hent bil efter id: `db.read(car_id)` → returnerer `Car`-objekt eller `None`
3. **READ_ALL** – Hent alle biler: `db.read_all()` → returnerer liste af `Car`-objekter
4. **SEARCH** – Søg efter biler: `db.search(term)` → returnerer liste af `Car`-objekter
5. **UPDATE** – Opdater bil: `db.update(car_id, car)` → returnerer `True`/`False`
6. **DELETE** – Slet bil: `db.delete(car_id)` → returnerer `True`/`False`

### Vigtige designvalg

- **`_run_query()`-metode** – Returnerer et dictionary med `"rows"` nøgle (som i eksemplet fra PDF'en)
- **Objekt-konvertering** – Alle metoder der søger i database konverterer resultaterne til `Car`-objekter
- **`sqlite3.Row`** – Aktiveret for at kunne konvertere database-rækker til dicts
- **`__str__()`** – Defineret i `Car`-klassen for pæn udskrivning

### Kørsel

```bash
python main.py
```

### Output-eksempel

```
=== OPRETTELSE (CREATE) ===
Oprettet: Toyota Corolla (id=1)
Oprettet: Volvo XC90 (id=2)
Oprettet: BMW X3 (id=3)

=== VIS ALLE (READ_ALL) ===
Bil: Toyota Corolla
År: 2020
---
Bil: Volvo XC90
År: 2022
...
```

### Testede operationer

✅ CREATE – Oprettelse af biler  
✅ READ – Hent enkelt bil  
✅ READ_ALL – Hent alle biler  
✅ SEARCH – Søg efter biler  
✅ UPDATE – Opdater bil  
✅ DELETE – Slet bil  
✅ __str__() – Pæn udskrivning af Car-objekt
