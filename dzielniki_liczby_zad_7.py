liczba = int(input("Podaj liczbę: "))
dzielniki = [] # tablica przechowująca dzielniki

# petla sprawdzajaca jakie sa dzielniki
for i in range(1, liczba+1):
    if liczba % i == 0:
        dzielniki.append(i)

print(f"Dzielniki liczby {liczba} to: {dzielniki}")