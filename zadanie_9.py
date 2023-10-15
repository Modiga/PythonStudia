saldo=0
print("Witaj w symulacji aplikacji bankowej!\nMożesz wykonać trzy operacje: wpłata, wypłata, sprawdzić saldo.\n")
while True:
    wybor=int(input("Którą operację chcesz wybrać:\n[1] Wpłata\n[2] Wypłata\n[3] Sprawdzić saldo\nNależy wybrać numer [1/2/3]: "))

    if wybor==1:
        ilosc=round(float(input("\nJaką kwotę chcesz wpłacić?\nKwota wpłaty: ")),2)
        saldo+=ilosc
        print(f"Wpłacono {ilosc}zł\n")
    elif wybor==2:
        ilosc=round(float(input("\nJaką kwotę chcesz wypłacić?\nKwota wypłaty: ")),2)
        if saldo-ilosc<0:
            print("Za mało środków na końcie!\n")
        else:
            saldo-=ilosc
            print(f"Wypłacono {ilosc}zł\n")
    elif wybor==3:
        print(f"Twoje saldo wynosi: {saldo}zł.\n")
    else:
        print("\nNależy podać odpowiednią cyfrę!\n")
    
    round(saldo,2)