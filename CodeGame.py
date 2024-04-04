from random import randint #Random Integer
from colorama import Fore

kods=[]
n=4

#For funkcija kas pievieno kodam četras nejauši izvēlētas vērtības vērtības
for i in range(n):
    kods.append(randint(0,9))

#Pārvērš vērtības sarakstā par string tālākai lietošanai
string_kods = [str(element) for element in kods]
# Pārbauda kāds kods tiek printēts
# print(*kods)

minejumu_skaits = 1

#Izmantojot join, apvieno sarakstu ar 4 cipariem vienā izmantojamā koda virknē.
x = "".join(str(num) for num in kods)

#Testēšanas nolūkam, iedots pirmais kods
# print(x)

while True:
    minejums = input(Fore.BLUE + f"Atmini 4 ciparu kodu!: ")
    if minejums.lower() == "stop":
        break
    elif x == minejums:
        print(Fore.GREEN + "Pareizi!")
        print(f"Tu uzminēji kodu {minejumu_skaits} minējumā/os!")
        for i in range(n):
            kods.clear()
            kods.append(randint(0,9))
        x = "".join(str(num) for num in kods)
    else:
        a = list(minejums)

        def cipari(saraksts1, saraksts2):
            pareizi = 0
            for item1, item2 in zip(saraksts1, saraksts2):
                if item1 == item2:
                    pareizi += 1
            return pareizi
        pareizi_cipari = cipari(string_kods, a)

        print(Fore.MAGENTA + f"Pareizi novietoti ir {pareizi_cipari} cipari no 4")
        minejumu_skaits += 1
print(Fore.YELLOW + "Paldies par spēlēšanu!")