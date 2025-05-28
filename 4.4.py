def palitra(color1, color2):
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        return "фиолетовый"
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        return "оранжевый"
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        return "зеленый"
    else:
        return None
color1 = input("Введите первый цвет для смешивания: ")
color2 = input("Введите второй цвет для смешивания: ")
if color1 in ["красный", "синий", "желтый"] and color2 in ["красный", "синий", "желтый"]:
    itog_color = palitra (color1, color2)
    print (f"при смешивании {color1} и {color2} получился {itog_color}.")
else:
    print ("неправельный базовый цвет")
palitra(color1, color2)