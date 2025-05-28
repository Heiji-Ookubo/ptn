import random
numbers_list = list(random.randint(1, 20) for i in range(5))
user_number = int(input("введите число"))
if user_number in numbers_list:
    print("Поздравляю вы угодали")
else:
    print("Нет ткого числа")
print(f"Исходный список {numbers_list}")
print(f"Ваше число {user_number}")
