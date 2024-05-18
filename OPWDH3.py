from abc import ABC, abstractmethod
from datetime import datetime

# Szoba absztrakt osztály
class Szoba(ABC):
    def __init__(self, ar: float, szobaszam: int):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def leir(self):
        pass

# EgyagyasSzoba konkrét osztály
class EgyagyasSzoba(Szoba):
    def __init__(self, ar: float, szobaszam: int):
        super().__init__(ar, szobaszam)

    def leir(self):
        return f"Egyágyas szoba {self.szobaszam}-as számú, ára: {self.ar} HUF"

# KetagyasSzoba konkrét osztály
class KetagyasSzoba(Szoba):
    def __init__(self, ar: float, szobaszam: int):
        super().__init__(ar, szobaszam)

    def leir(self):
        return f"Kétágyas szoba {self.szobaszam}-as számú, ára: {self.ar} HUF"

# Szalloda osztály
class Szalloda:
    def __init__(self, nev: str):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba: Szoba):
        self.szobak.append(szoba)

# Foglalas osztály
class Foglalas:
    def __init__(self, szoba: Szoba, datum: datetime):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Foglalás: {self.szoba.leir()}, dátum: {self.datum.strftime('%Y-%m-%d')}"

# Foglalasok Kezelese
class FoglalasKezelo:
    def __init__(self, szalloda: Szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglal(self, szobaszam: int, datum: datetime):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        print("A szoba már foglalt ezen a napon.")
                        return None
                uj_foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(uj_foglalas)
                print(f"Foglalás sikeres: {uj_foglalas}")
                return szoba.ar
        print("Nincs ilyen szobaszám.")
        return None

    def lemond(self, szobaszam: int, datum: datetime):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print(f"Foglalás lemondva: {foglalas}")
                return True
        print("Nem található ilyen foglalás.")
        return False

    def listaz(self):
        if not self.foglalasok:
            print("Nincs foglalás.")
        for foglalas in self.foglalasok:
            print(foglalas)

# Felhasználói interfész
def felhasznaloi_interface():
    szalloda = Szalloda("Hotel Budapest")
    szalloda.add_szoba(EgyagyasSzoba(10000, 101))
    szalloda.add_szoba(EgyagyasSzoba(12000, 102))
    szalloda.add_szoba(KetagyasSzoba(15000, 201))

    kezelo = FoglalasKezelo(szalloda)
    kezelo.foglal(101, datetime(2024, 5, 20))
    kezelo.foglal(102, datetime(2024, 5, 21))
    kezelo.foglal(201, datetime(2024, 5, 22))
    kezelo.foglal(101, datetime(2024, 5, 23))
    kezelo.foglal(102, datetime(2024, 5, 24))

    while True:
        print("\n--- Foglalási Rendszer ---")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy opciót: ")

        if valasztas == "1":
            szobaszam = int(input("Szobaszám: "))
            datum_str = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                datum = datetime.strptime(datum_str, '%Y-%m-%d')
                if datum < datetime.now():
                    print("A dátumnak jövőbeni dátumnak kell lennie.")
                else:
                    ar = kezelo.foglal(szobaszam, datum)
                    if ar is not None:
                        print(f"A foglalás ára: {ar} HUF")
            except ValueError:
                print("Érvénytelen dátum formátum. Használja az ÉÉÉÉ-HH-NN formátumot.")
        elif valasztas == "2":
            szobaszam = int(input("Szobaszám: "))
            datum_str = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                datum = datetime.strptime(datum_str, '%Y-%m-%d')
                kezelo.lemond(szobaszam, datum)
            except ValueError:
                print("Érvénytelen dátum formátum. Használja az ÉÉÉÉ-HH-NN formátumot.")
        elif valasztas == "3":
            kezelo.listaz()
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    felhasznaloi_interface()