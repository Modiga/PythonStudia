import random

print("Witaj w prostym kalkulatorze!")
# petla pobierajaca dane od uzytkownika
while True:
    podaneLiczby=[] # tablica przechowujaca podane liczby
    for i in range(2):
        czyLosowa=input("Czy chcesz losować liczbę z podanego zakresu [T/N]: ")
        if czyLosowa=="T":
            liczbaPoczatkowa=int(input("Podaj swoją 1. liczbę zakresu: "))
            liczbaKonczaca=int(input("Podaj swoją 2. liczbę zakresu: "))
            liczba=float(random.randrange(liczbaPoczatkowa,liczbaKonczaca))
        else: 
            liczba=float(input(f"Podaj swoją {i+1}. liczbę: "))
        podaneLiczby.append(liczba)

    print("Wybierz jakie działanie chcesz wykonać:\n[+] dodawanie\n[-] odejmowanie\n[*] mnożenie\n[/] dzielenia\n[#] potęgowanie\n[^] pierwiastkowanie")
    wybor=input("Wpisz jeden z symboli: ")

    if wybor=="+":
        print("Wynik dodawania: {}".format(podaneLiczby[0]+podaneLiczby[1]))
    elif wybor=="-":
        print("Wynik odejmowania: {}".format(podaneLiczby[0]-podaneLiczby[1]))
    elif wybor=="*":
        print("Wynik mnożenia: {}".format(podaneLiczby[0]*podaneLiczby[1]))
    elif wybor=="/":
        print("Wynik dzielenia: {}".format(podaneLiczby[0]/podaneLiczby[1]))
    elif wybor=="#":
        print("Wynik potęgowania: {}".format(podaneLiczby[0]**podaneLiczby[1]))
    elif wybor=="^":
        print("Wynik pierwiastkowania: {}".format(podaneLiczby[0]**(1/podaneLiczby[1])))
    else:
        print("\nReset programu, ponieważ podałeś zły symbol!\n")
        continue
    
    czyNoweDane=input("Czy chcesz podać nowe dane? [T/N]: ")
    if czyNoweDane=="T":
        continue
    else:
        break