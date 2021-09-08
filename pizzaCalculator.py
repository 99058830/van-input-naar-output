#Jordy van Zomeren, 99058830, Pizza calculator

#Bewaren van prijzen
small = 5.95
medium = 7.95
large = 9.95

print(""" #Print simpel onderstaand menu
|------------------------------------------------
|                    ONS MENU
|------------------------------------------------
|                     SMALL
|                  20cm | 5,95 euro
|------------------------------------------------
|                     MEDIUM
|                  25cm | 7,95 euro
|------------------------------------------------
|                     LARGE
|                  30cm | 9,95 euro              
|------------------------------------------------
""")

#Input voor de hoeveelheid
hoeveelSmall = int(input("Aantal small size pizza's "))
hoeveelMedium = int(input("Aantal medium size pizza's "))
hoeveelLarge = int(input("Aantal large size pizza's "))

#Reken sommen die uitgevoerd moeten worden
allPrice = hoeveelSmall * small + hoeveelMedium * medium + hoeveelLarge * large
prijsSmall = hoeveelSmall * small
prijsMedium = hoeveelMedium * medium
prijsLarge = hoeveelLarge * large

#print en uitkomst van de prijzen die opgetelt zijn door de bovenstaande rekensom
print("""
|------------------------------------------------
|Small hoeveelheid    :""",hoeveelSmall,"""
|Small prijs totaal   :""",prijsSmall,"""euro
|------------------------------------------------
|Medium hoeveelheid   :""",hoeveelMedium,"""
|Medium prijs totaal  :""",prijsMedium,"""euro
|------------------------------------------------
|Large hoeveelheid    :""",hoeveelLarge,"""
|Large prijs totaal   :""",prijsLarge,"""euro
|------------------------------------------------
|Te betalen           :""",allPrice,"""euro
|------------------------------------------------
""")