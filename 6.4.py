def fvgh():
    bilet = input("введите номер билета: ")
    bilet_1 = ""
    bilet_2 = ""
    if len(bilet)%2==0:
        bilet_1 = bilet[:int(len(bilet) / 2)]
        bilet_2 = bilet[int(len(bilet) / 2):]
        sum_1 = 0
        sum_2 = 0
        for i in bilet_1:
            sum_1 += int(i)
        for i in bilet_2:
            sum_2 += int(i)
        if sum_1 == sum_2:
            print(f"Билет: {bilet} счасливый")
        else:
            print(f"Билет: {bilet} не счасливый")
    else:
        print(f"Билет: {bilet} не существует")