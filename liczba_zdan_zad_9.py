# Importowanie modułu odpowiedzialnego za wyrażenia regularne
import re

def liczba_zdan(tekst):
    # Tworzenie obiektu wyrażenia regularnego, [.!?] to zestaw znaków, który oznacza dowolny znak
    wzor = re.compile(r'[.!?]')

    # Znajdywanie wszystkich wystąpień
    wystapienia = re.findall(wzor, tekst)

    # Liczba zdań to liczba znalezionych wystąpień.
    return len(wystapienia)

def main():
    # Wczytaj tekst z pliku
    nazwa_pliku = 'tekst.txt'
    with open(nazwa_pliku, 'r') as plik:
        tekst = plik.read()

    # Zlicz liczbę zdań
    ilosc_zdan = liczba_zdan(tekst)

    # Wyświetl wynik
    print(f"Liczba zdań w tekście: {ilosc_zdan}")

main() # Start programu (*^_^*)



# DODATKOWE INFO

# Link do generowania przykładowego tekstu: https://anytexteditor.com/pl/text-generator

# Tak wygląda print(wystapienia): ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']