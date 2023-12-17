class Punkt1:
    pass

class Punkt2:
    pass

def czy_istnieje_kwadrat(dane):
    if len(dane) < 4:
        return False  # Zbyt mało punktów, nie można utworzyć kwadratu
    
    for i in range(len(dane)):
        Punkt1.x, Punkt1.y = dane[i]
        for j in range(i+1, len(dane)):
            Punkt2.x, Punkt2.y = dane[j]
            if Punkt1.x != Punkt2.x and Punkt1.y != Punkt2.y:
                # Szukamy dwóch punktów, które nie leżą na jednej prostej (nie mają wspólnych współrzędnych x ani y)
                # oraz sprawdzamy, czy istnieją dwa punkty o współrzędnych Punkt1.x, Punkt2.y i Punkt2.x, Punkt1.y (równe boki)
                if (Punkt1.x, Punkt2.y) in dane and (Punkt2.x, Punkt1.y) in dane:
                    print(f"Współrzędne kwadratu: ({Punkt1.x},{Punkt1.y}), ({Punkt1.x},{Punkt2.y}), ({Punkt2.x},{Punkt2.y}), ({Punkt2.x},{Punkt1.y})")
                    # Sprawdzamy, czy żadne inne punkty nie leżą wewnątrz kwadratu
                    for k in range(len(dane)):
                        x3, y3 = dane[k]
                        if (Punkt1.x < x3 < Punkt2.x or Punkt2.x < x3 < Punkt1.x) and (Punkt1.y < y3 < Punkt2.y or Punkt2.y < y3 < Punkt1.y):
                            return False # Punkty w środku
                    return True # Kwadrat bez punktów w środku
    return False # Nie ma kwadratu

# Program
dane = [(-3, -3), (-2, -2), (-1, -1), (-1,-3), (-3, -1), (1, 1), (2, 2), (3, 3), (4, 4), (0, 5), (5, 0), (5, 5), (2, 5), (5, 2), (6, 6), (7, 7)]
wynik = czy_istnieje_kwadrat(dane)
print(wynik)