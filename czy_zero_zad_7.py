# Zadanie 7.
# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n wypełnioną liczbami naturalnymi. Dla danej tablicy należy napisać funkcję, która będzie zwracała wartość True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość False w przeciwnym przypadku. Wymiar tablicy powinien być definiowany przez użytkownika.

# Zdefiniowana klasa żeby obsłużyc błąd
class LiczbaNiedodatniaError(Exception):
    pass

def wczytaj_tablice(n):
    tablica = []
    for i in range(n):
        wiersz = []
        for j in range(n):
            while True:
                try:
                    liczba = float(input(f"Podaj element tablicy na pozycji ({i+1}, {j+1}): "))
                    break
                except ValueError:
                    print("Błąd! Wprowadź liczbę.")
            wiersz.append(liczba)
        tablica.append(wiersz)
    return tablica

def czy_wystepuje_zero(tablica):
    n = len(tablica)
    
    # Sprawdzenie wierszy
    for i in range(n):
        if 0 not in tablica[i]:
            return False
    
    # Sprawdzenie kolumn
    for j in range(n):
        kolumna = [tablica[i][j] for i in range(n)]
        if 0 not in kolumna:
            return False
    
    return True

# Wczytaj wymiar tablicy od użytkownika
while True:
    try:
        n = int(input("Podaj wymiar tablicy: "))
        if n <= 0:
            raise LiczbaNiedodatniaError()# Wywołanie błędu
        break
    except ValueError:
        print("Podaj liczbę naturalną!")
    except LiczbaNiedodatniaError:
            print("Liczba powinna być dodatnia!")

# Wczytaj tablicę dwuwymiarową o wymiarze n x n
tablica_dwuwymiarowa = wczytaj_tablice(n)

# Sprawdź zera
wynik = czy_wystepuje_zero(tablica_dwuwymiarowa)

# Wyświetl wynik
if wynik:
    print("W każdym wierszu i kolumnie występuje co najmniej jedno 0.")
else:
    print("Nie w każdym wierszu i kolumnie występuje co najmniej jedno 0.")