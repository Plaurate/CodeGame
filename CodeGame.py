from random import randint #Random Integer
from colorama import Fore, Back, Style

kods=[]
n=4

#Noteikumi
print(Fore.LIGHTYELLOW_EX + "Spēlē tev ir jāatmin 4 ciparu kods. ir pateikts cik cipari ir pareizā vietā un beigās minējumu skaits kad tu uzmini kodu. Kad tu to uzmini, ir jauns kods kuru atkal ir jāmin. ")
print("Lai beigtos spēle, uzraksti 'Stop'"+ Fore.RESET)

#For funkcija kas pievieno kodam četras nejauši izvēlētas vērtības vērtības
for i in range(n):
    kods.append(randint(0,9))


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
        print(f"Tu uzminēji kodu {minejumu_skaits} minējumā/os! Turpini minēt jaunu skaitli:")
        for i in range(n):
            kods.clear()
            kods.append(randint(0,9))
        x = "".join(str(num) for num in kods)
    else:
        a = list(minejums)
        #Pārvērš vērtības sarakstā par string tālākai lietošanai
        string_kods = [str(element) for element in kods]
        def cipari(saraksts1, saraksts2):
            pareizi = 0
            for item1, item2 in zip(saraksts1, saraksts2):
                if item1 == item2:
                    pareizi += 1
            return pareizi
        pareizi_cipari = cipari(string_kods, a)

        print(Fore.MAGENTA + f"Pareizi novietoti ir {pareizi_cipari} cipari no 4")
        minejumu_skaits += 1
print(Fore.YELLOW + Style.BRIGHT + Back.RED + "Paldies par spēlēšanu!" + Fore.RESET + Style.NORMAL + Back.RESET)