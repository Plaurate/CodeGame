from random import randint #Random Integer

kods=[]
n=4

#For funkcija kas pievieno kodam četras nejauši izvēlētas vērtības vērtības
for i in range(n):
    kods.append(randint(0,9))

# Pārbauda kāds kods tiek printēts
# print(*kods)

minejumu_skaits = 0

#Izmantojot join, apvieno sarakstu ar 4 cipariem vienā izmantojamā koda virknē.
x = "".join(str(num) for num in kods)
print(x)


pareizi_cipari = 0

while True:
    minejums = input(f"Atmini 4 ciparu kodu!: ")
    if minejums.lower() == "stop":
        break
    elif x == minejums:
        print("Pareizi!")
        print(f"Tu uzminēji kodu {minejumu_skaits} minējumos!")
        for i in range(n):
            kods.clear()
            kods.append(randint(0,9))
        x = "".join(str(num) for num in kods)
    else:
        
        a = list(minejums)
        if a[0] == kods[0]:
           pareizi_cipari = pareizi_cipari + 1 

        print(f"Pareizi novietoti ir {pareizi_cipari} cipari no 4")
        minejumu_skaits += 1
print("Paldies par spēlēšanu!")