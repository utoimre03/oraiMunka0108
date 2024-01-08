def hossz():
    szo1 = input("\tKérek egy szót: ")
    szo2 = input("\tKérek egy másik szót: ")

    szo1Hossz = len(szo1)
    szo2Hossz = len(szo2)

    print("I/a.")
    if szo1Hossz < szo2Hossz:
        print(f"\tA hosszabb szó: {szo2}.")
    elif szo1Hossz > szo2Hossz:
        print(f"\tA hosszabb szó: {szo1}.")
    else:
        print("\tEgyenlő hosszúak.")

    print("I/d.")
    kulonbseg = abs(szo1Hossz-szo2Hossz)
    print(f"\tA szavak hosszának a különbsége: {kulonbseg}")