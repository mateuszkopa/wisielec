#podaj slowo
print("Podaj słowo")
slowo = input()

#zmienne
zycie = 7
tablica = list(slowo)
print("Gra w wisielca")

#zamiana słowa na podkreślenia
for i in range(len(slowo)):
    tablica[i] = "_"

#pętla która działa tak długo dopóki życie jest większe od 0
while zycie > 0:
    #odziela spacją wyraz z tablicy
    print(" ".join(tablica))
    #wpisywana litera
    print("Wpisz literę: ")
    litera = input()
    print("pozostało ci: ", zycie, "żyć")

    #udało się odgadnąć literę
    if litera in slowo:
        #zmieniamy znak podkreślenia na literę
        for i in range(len(slowo)):
            if slowo[i] == litera:
                tablica[i] = litera
                #sprawdzamy czy tablica jest równa hasłu
        if "".join(map(str,tablica)) == slowo:
            print("Wygrałeś!")
            break
    else:
        #tracimy życie jeżeli litera nie jest w slowie
        zycie -= 1
        if zycie < 1:
            print("Przegrałeś!")
