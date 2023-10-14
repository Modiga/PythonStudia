podaneLiczby=[] # tablica przechowujaca podane liczby

# petla pobierajaca dane od uzytkownika
for i in range(2):
    liczba=int(input(f"Podaj swoją {i+1}. liczbę: "))
    podaneLiczby.append(liczba)
    
# warunek ktory sprawdza ktora liczba jest wieksza i na tej podstawie tworzy tablice z zakresem
if podaneLiczby[1]>podaneLiczby[0]:
    zakres=[*range(podaneLiczby[0], podaneLiczby[1]+1, 1)]
else:
    zakres=[*range(podaneLiczby[1], podaneLiczby[0]+1, 1)]

# warunek ktory sprawdza czy zakres jest wiekszy niz 20 i wyswietla dane w odpowiedni sposob
if len(zakres)<=20:
    print(f"\nLiczby całkowite znajdujące się w twoim zakresie <{zakres[0]}, {zakres[len(zakres)-1]}>:")
    for liczba in zakres:
        print(liczba, end=" ")
else:
    # wyliczanie sredniej
    suma=0
    for liczba in zakres:
        suma+=liczba
    srednia=round(suma/len(zakres)) # zaokraglenie do calkowitej

    # wyszukawanie liczb najblizej sredniej
    if srednia in zakres:
        pozycja=zakres.index(srednia)

        print("\nZakres jest większy niż 20, dlatego wypisuję tylko 6 liczb z tego zakresu, które są najbliżej średniej (bez samej średniej)")
        for i in range(7):
            y=-3+i
            if y==0: continue
            print(zakres[pozycja+y], end=" ")