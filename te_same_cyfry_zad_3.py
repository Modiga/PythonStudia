import random

# zdefiniowana klasa zeby obsluzyc blad
class LiczbaUjemnaError(Exception):
    pass

#funkcja do wczytania liczb
def podawanie_liczb():
    while True:
        podane_liczby=[0]*3
        try:
            for _ in range(3):
                liczba = int(input(f"Podaj {_+1}. liczbę całkowitą: "))
                if liczba < 0:
                    raise LiczbaUjemnaError()#wywolanie bledu
                podane_liczby[_]=liczba

            break
        except ValueError:
            print("Podano nieprawidłową wartość!")
        except LiczbaUjemnaError:
            print("Liczba powinna być dodatnia!")

    return podane_liczby

# funkcja wypisujaca cyfry z ktorych jest liczba
def sprawdz_cyfry(liczba):
    cyfry = set([*str(liczba)])
    return cyfry

#funkcja generujaca zestaw z 3 liczbami ktorych mozna uzyc
def generuj_liczby(liczba, nowe_cyfry):
    while True:
        wygenerowane_liczby = []
        for _ in range(3):
            nowa_liczba=""
            dlugosc_liczby=len(str(liczba))
            if dlugosc_liczby<3:
                dlugosc_liczby=random.randint(0,10)
            for __ in range(dlugosc_liczby):
                i = random.randint(0,len(nowe_cyfry)-1) 
                nowa_liczba+=list(nowe_cyfry)[i]
            wygenerowane_liczby.append(nowa_liczba)

        cyfry_generowane1 = sprawdz_cyfry(wygenerowane_liczby[0])
        cyfry_generowane2 = sprawdz_cyfry(wygenerowane_liczby[1])
        cyfry_generowane3 = sprawdz_cyfry(wygenerowane_liczby[2])
        if sorted(cyfry_generowane1) == sorted(cyfry_generowane2) == sorted(cyfry_generowane3):
            return wygenerowane_liczby

# DZIAŁANIE PROGRAMU

podane_liczby = podawanie_liczb()

cyfry_liczby1 = sprawdz_cyfry(podane_liczby[0])
cyfry_liczby2 = sprawdz_cyfry(podane_liczby[1])
cyfry_liczby3 = sprawdz_cyfry(podane_liczby[2])

# obsluzenie przypadku dla liczb z tych samych cyfr
if sorted(cyfry_liczby1) == sorted(cyfry_liczby2) == sorted(cyfry_liczby3):
    print("Podane liczby są zbudowane z takich samych cyfr.")
else:
    print("Podane liczby nie są zbudowane z takich samych cyfr.\nMoże chciałbyś skorzystać z następujących liczb:")
    wygenerowane1 = generuj_liczby(podane_liczby[0], cyfry_liczby1)
    wygenerowane2 = generuj_liczby(podane_liczby[1], cyfry_liczby2)
    wygenerowane3 = generuj_liczby(podane_liczby[2], cyfry_liczby3)
    print("Zestaw dla liczby 1:", wygenerowane1)
    print("Zestaw dla liczby 2:", wygenerowane2)
    print("Zestaw dla liczby 3:", wygenerowane3)



#bład dla tylko wielkich liczb, np: 98769689689687798789898769879698679789769869679879798769769867989768698697896798798698698976987967896789689679879789789876987697987897869867987978976979898976896789797898769789876968968968779878989876987969867978976986967987979876976986798976869869789679879869869897698796789678968967987978978987698769798789786986798797897697989897689678979789876978