def mag_data():
    data = input("Введите дату в формате дд.мм.гггг.")
    day, month, year = map(int, data.split('.'))
    prod = day * month
    last = year % 100
    if prod == last:
        print("Дата магическая")
    else:
        print("Дата не магическая")
mag_data()