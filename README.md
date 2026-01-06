# Bil Database System (Programmering B) – OOP & GUI

Dette projekt er en komplet CRUD-applikation (Create, Read, Update, Delete) til håndtering af bil-data. Systemet er opbygget omkring objektorienterede principper, hvor en SQLite-database integreres med en grafisk brugerflade bygget i Tkinter.

## 📂 Filoversigt

* **`car.py`**: Definerer `Car`-klassen, som fungerer som systemets entitet. Den indeholder attributter for id, mærke, model og årgang samt en `__str__`-metode til formatering.
* **`database.py`**: Håndterer al SQL-logik og database-kommunikation. Klassen sørger for at konvertere database-rækker direkte til `Car`-objekter.
* **`main.py`**: Applikationens kontrolcenter og brugerflade. Den indeholder al logik for at skabe vinduer, knapper og tekstfelter via `tkinter`.

## 🖥️ Den Nye Grafiske Brugerflade (GUI)

Applikationen er nu opgraderet fra et terminal-script til en fuld interaktiv GUI. 



### Funktioner i hovedmenuen:
* **Opret bil (CREATE)**: Åbner et pop-up vindue til indtastning af en ny bils specifikationer.
* **Find bil (READ)**: Gør det muligt at søge efter en specifik bil baseret på dens unikke ID.
* **Vis alle biler (READ ALL)**: Henter samtlige biler fra databasen og viser dem i det centrale tekstfelt.
* **Opdater bil (UPDATE)**: Gør det muligt at redigere oplysningerne for en eksisterende bil via ID.
* **Slet bil (DELETE)**: Fjerner en bil permanent fra databasen.
* **Søg bil (SEARCH)**: Dynamisk søgning efter biler baseret på mærke eller modelnavn.

### Tekniske detaljer i GUI-implementeringen:
* **Toplevel-vinduer**: Hver operation åbner i sit eget dedikerede vindue for at holde hovedmenuen ren og overskuelig.
* **Feedback-felt**: Et `Text`-objekt i bunden af hovedvinduet fungerer som konsol, der viser resultater og bekræftelser til brugeren.
* **Fejlhåndtering**: Programmet bruger `messagebox` til at give advarsler, hvis brugeren f.eks. indtaster tekst i et tal-felt.

## 🛠️ Tekniske Designvalg

* **SQLite Integration**: Databasen bruger `sqlite3.Row` factory for at kunne behandle resultater som dictionaries.
* **Abstraktion**: Al SQL kørsel er samlet i en intern `_run_query` metode for at mindske gentagelser i koden.
* **Automatisk nulstilling**: Ved opstart sletter `main.py` den eksisterende `cars.db` fil for at sikre et rent testmiljø (dette kan fjernes i produktionsbrug).

## 🚀 Kørsel af programmet

For at starte applikationen skal du køre:

```bash
python main.py