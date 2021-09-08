Croissant = 0.39
Kortingsbon = 0.50
Stokbrood = 2.78
hoeveelCroissant = int(input('Aantal croissanten'))
hoeveelStokbrood = int(input('Aantal strokbroden'))
hoeveelKortingsbon = int(input('Aantal kortingsbonnen'))

if hoeveelKortingsbon >= 1: 
    Prijs = hoeveelCroissant  *Croissant + hoeveelStokbrood * Stokbrood - hoeveelKortingsbon * Kortingsbon
    Centen = int(Prijs) * 100
    print("De feestlunch kost je bij de bakker", Centen, "cent voor", hoeveelCroissant,  "croissantjes en de", hoeveelStokbrood, "stokbroden als de", hoeveelKortingsbon, "kortingsbonnen nog geldig zijn!")
else:
    Prijs = hoeveelCroissant * Croissant + hoeveelStokbrood * Stokbrood
    Centen = int(Prijs) * 100
    print("De feestlunch kost je bij de bakker", Centen, "cent voor", hoeveelCroissant,  "croissantjes en de", hoeveelStokbrood, "stokbroden!")

