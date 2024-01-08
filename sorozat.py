import random

def letrehoz(szam1: int, szam2: int):
    print("II/a.")
    print("\t", end="")
    # lista létrehozása
    lista = []
    if szam1 < szam2:
        kisebb = szam1
        nagyobb = szam2
    else:
        kisebb = szam2
        nagyobb = szam1
    for szamom in range(1, 16, 1):
        szam = random.randint(kisebb, nagyobb)
        lista.append(szam)
    # kiírás
    # utolsó elem megkülönböztetés módszerével
    for index in range(0, len(lista), 1):
        if index == len(lista)-1:
            # utolsó elem
            print(lista[index])
        else:
            # összes többi elem
            print(f"{lista[index]}%", end="")
    # visszatérési érték
    return lista

def legkisebb(lista):
    print("II/b.")
    kiFile = open("legkisebb.txt", "w", encoding="UTF-8")
    print("\tA legkisebb elem: ", end="")
    print("\tA legkisebb elem: ", end="", file=kiFile)
    # minimum keresés tétele
    minErtek = lista[0]
    minHely = 0
    index = 1
    while index < len(lista):
        if lista[index] < minErtek:
            minErtek = lista[index]
            minHely = index
        index += 1
    print(f"{minErtek}.")
    print(f"{minErtek}.", file=kiFile)
