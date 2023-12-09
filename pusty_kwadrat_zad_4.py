def czy_istnieje_kwadrat(dane):
    if len(dane) < 4:
        return False  # Zbyt mało punktów, nie można utworzyć kwadratu
    
    for i in range(len(dane)):
        x1, y1 = dane[i]
        for j in range(i+1, len(dane)):
            x2, y2 = dane[j]
            if x1 != x2 and y1 != y2:
                # Szukamy dwóch punktów, które nie leżą na jednej prostej (nie mają wspólnych współrzędnych x ani y)
                # oraz sprawdzamy, czy istnieją dwa punkty o współrzędnych x1, y2 i x2, y1 (równe boki)
                if (x1, y2) in dane and (x2, y1) in dane:
                    print(f"Współrzędne kwadratu: ({x1},{y1}), ({x1},{y2}), ({x2},{y2}), ({x2},{y1})")
                    # Sprawdzamy, czy żadne inne punkty nie leżą wewnątrz kwadratu
                    for k in range(len(dane)):
                        x3, y3 = dane[k]
                        if (x1 < x3 < x2 or x2 < x3 < x1) and (y1 < y3 < y2 or y2 < y3 < y1):
                            return False # Punkty w środku
                    return True # Kwadrat bez punktów w środku
    return False # Nie ma kwadratu

# Program
dane = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (0, 5), (5, 0), (5, 5), (2, 5), (5, 2), (6, 6), (7, 7)]
wynik = czy_istnieje_kwadrat(dane)
print(wynik)