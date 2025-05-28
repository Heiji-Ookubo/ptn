from random import randint
group_1 = ["Фоминых", "Лаптев", "Альникина", "Ридер", "Санникова", "Хайбулина", "Карнильева", "Попова", "Еньшин", "Алияров"]
group_2 = ["Горшенёв", "Яльцев", "Васильев", "Дыбенко", "Новичихин", "Форгов", "Баранов", "Андреев", "Куценко", "Иванов"]
tupi = (group_1[randint(0, 9)], group_1[randint(0, 9)], group_1[randint(0, 9)], group_1[randint(0, 9)], group_1[randint(0, 9)], group_2[randint(0, 9)], group_2[randint(0, 9)], group_2[randint(0, 9)], group_2[randint(0, 9)], group_2[randint(0, 9)])
tupi_list = [x for x in tupi]
print(tupi, len(tupi))
tupi_list.sort()
print(tupi_list)
count = 0
if "Иванов" in tupi:
    count += tupi.count("Иванов")
print(count)
print (group_1)
print (group_2)