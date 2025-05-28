def delenie(num):
    if num % 3 == 0:
        return True
    else:
        return False
    try:
        vvod=int(input("введите число: "))
        if delenie(vvod):
            print(f"{vvod} делиться на 3")
        else:
            print(f"{vvod} делиться на 3")
    except ValueError:
        print("Пожалуйста введите целое число.")
def main():
    try:
        num = input("введите число на которое будите делить 100: ")
        result = 100 / num
        print(f"100 делиться на {num} равно {result}")
    except ValueError:
        print("Пожалуйста введите целое число.")
    except ZeroDivisionError:
        print("Деление на 0 неозможно.")

def mag_data():
    data = input("Введите дату в формате дд.мм.гггг.")
    day, month, year = map(int, data.split('.'))
    prod = day * month
    last = year % 100
    if prod == last:
        print("Дата магическая")
    else:
        print("Дата не магическая")

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

fvgh() , mag_data()