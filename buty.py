but1 = float(input("Podaj cene buta 1: "))
but2 = float(input("Podaj cene buta 2: "))
but2 = float(0.8 * but2)
print(but2)

if but1 + but2 > 399:
    cena = 0.8 * (but1 + but2)
    bonyfikata = True
else:
    cena = but1 + but2
    bonyfikata = False

print(f"Zaplacisz {round(cena, 2)} zł")
a = cena / 1.23
podatek = cena - a
print(f"Podatek {round(podatek, 2)} zł")
if bonyfikata == True:
    print("Dostaniesz rabat")
else:
    print("Nie dostaniesz")
