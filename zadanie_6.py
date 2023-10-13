podaneLiczby=[] # tablica przechowujaca podane liczby

# petla pobierajaca dane od uzytkownika
for i in range(2):
    liczba=float(input(f"Podaj swoją {i+1}. liczbę: "))
    podaneLiczby.append(liczba)

# warunek konczy program w przypadku 2 liczb mniejszych od 0
if podaneLiczby[0]<0 and podaneLiczby[1]<0:
    print("Obie liczby są mniejsze niż zero. Koniec programu.")

# petlla wychwytuje mozliwa liczbe mniejsza od zera i bierze jej wartosc bezwzgledna
for liczba in podaneLiczby:
    if liczba<0:
        liczba=liczba*(-1)

print("\nTeraz podam wyniki działań dla twoich liczb:")# komunikat przed wynikami

print("Suma: {}".format(podaneLiczby[0]+podaneLiczby[1]))# suma liczb
print("Różnica: {}".format(podaneLiczby[0]-podaneLiczby[1]))# roznica liczb

"""
Ponizszy kod dziala nastepujaco:
wynik mnozenia liczb
srawdzenie czy wynik wynosi 10, jezeli tak dodaje Yay!
wyswietla iloczyn liczb
"""
iloczynLiczb=podaneLiczby[0]*podaneLiczby[1]
jej="Yay!" if iloczynLiczb==10 else ""
print("Iloczyn: {} {}".format(iloczynLiczb, jej))

print("Iloraz: {}".format(podaneLiczby[0]/podaneLiczby[1]))# iloraz liczb

# kwadraty obu liczb
print("Kwadrat 1. liczby: {}".format(podaneLiczby[0]*podaneLiczby[0]))
print("Kwadrat 2. liczby: {}".format(podaneLiczby[1]*podaneLiczby[1]))

#pierwiastki kwadratowe obu liczb
print("Pierwiastek kwadratowy 1. liczby: {}".format(podaneLiczby[0]**(1/2)))
print("Pierwiastek kwadratowy 2. liczby: {}".format(podaneLiczby[1]**(1/2)))