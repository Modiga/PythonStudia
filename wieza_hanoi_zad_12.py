def hanoi(n, zrodlo, cel, pomoc):
    if n > 0:
        # Przenieś n-1 krążków z źródła do pomocniczego
        hanoi(n-1, zrodlo, pomoc, cel)
        
        # Przenieś n-ty krążek z źródła do celu
        print(f"Przenieś krążek {n} z {zrodlo} do {cel}")
        
        # Przenieś n-1 krążków z pomocniczego do celu
        hanoi(n-1, pomoc, cel, zrodlo)

# Przykład użycia dla x krążków na wieży S, przenosząc je na wieżę C, z użyciem wieży P jako pomocniczej
hanoi(4, 'S', 'C', 'P')


# Wideo: https://youtu.be/iG4lHkfuu8I?t=618