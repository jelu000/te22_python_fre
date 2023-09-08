# Denna uppgift ska vi öva variabler, vilkor och loopar
import random
import os
os.system("cls" if os.name == "nt" else "clear")

print("\n---------------------------------------------")
print(".:GissaTalet:.")

print("gissa ett tal mellan 1 - 10 och pröva lyckan, du får 3st försök!\n")

slumptal = random.randint(1, 10)
print(slumptal)

i=0
hitta = False

#loopar

while i < 3:

    gissatal = input("mata in tal: ")

    if slumptal == int(gissatal):
        hitta = True
        print("\n Rätt svar! \n")
        break
    
    if (slumptal > int(gissatal)):
        print(f"talet är större än {gissatal}")
    elif (slumptal < int(gissatal)):
        print(f"talet är mindre än {gissatal}")

    print(f"Du har {2-i} försök kvar")

    i += 1

if hitta:
    print("\n Bra jobbat, här får du en anka \U0001F609")

else:
    print("Bättre lycka nästa gång")

print("\n------------------------------------------------------------")