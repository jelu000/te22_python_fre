#visar vad funktioner är, vad de har för nytta, främst för att slippa repetera kod och samla koden block
#går även igenom arrayer är

import random

#skapar en Tuple typ av samling
frukter = ("Banan", "Melon", "Kiwi", "Citron")
looping = True

#Definerar python funktion
def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " kommer här\n")


while looping:
    print("____________________________________________________________")



    i=0

    for frukt in frukter:
        print(f"{str(i+1)} : {frukt}")
        i += 1


    fruktnr =  input("\n Mata in nummer på frukt du vill ha: ")

    print_fruit(fruktnr)

    go = input("Vill du välja en frukt till? j/n : ")
    print("\n")

    if go == "n":
        break

