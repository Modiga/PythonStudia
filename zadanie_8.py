import random

liczba = int(input("Podaj liczbę całkowitą nieujemną: "))# zmienna z podana liczba od uzytkownika


# petla generujaca choinke
for i in range(1, liczba + 1):
    spacje = " " * (liczba - i)
    gwiazdki = "*" * (2 * i - 1)# tworzy rzad gwiazdek
    # warunek ktory dodaje bombki jezeli gwiazdek jest wiecej niz 2
    if len(gwiazdki)>2:
        losowa=random.randint(0,len(gwiazdki)-1)# generuje losowa pozycje bombki
        gwiazdki=[*gwiazdki]
        gwiazdki[losowa]="o"
        gwiazdki=''.join(gwiazdki)
    print(spacje + gwiazdki)# wyswietla rzad choinki

# dodaje pien
spacje = " " * (liczba - 1)
print(spacje + "U")