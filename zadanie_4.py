imie="Maciej"
nazwisko="Drzazga"
wiek=19
ulubionaPotrawa="firmowy kotlet schabowy ze stołówki studenckiej"
ulubioneZwierze="królik"
wynikDzielenia=5/7

print("Nazywam się {} {}. Mam {} lat. Moją ulubioną potrawą jest {}. Najlepsze zwierzę to zdecydowanie {}.".format(imie, nazwisko, wiek, ulubionaPotrawa, ulubioneZwierze))
print("Na koniec wynik dzielenia: {}".format("%.2f" % round(wynikDzielenia, 2)))

print("\n------ TERAZ BEZ ZMIENNYCH ------\n")

print("Nazywam się {} {}. Mam {} lat. Moją ulubioną potrawą jest {}. Najlepsze zwierzę to zdecydowanie {}.".format("Maciej", "Drzazga", 19, "firmowy kotlet schabowy ze stołówki studenckiej", "królik"))
print("Na koniec wynik dzielenia: {}".format("%.2f" % round(5/7, 2)))