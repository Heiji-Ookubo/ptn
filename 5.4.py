import random
def mat_game():
    pr_otv = 0
    npr_otv = 0
    while npr_otv < 3:
        num1 = random.randint (1, 10)
        num2 = random.randint(1, 10)
        expression = f"{num1} + {num2}= "
        try:
            user_otv=int(input(expression))
        except ValueError:
            print ("Пожалуйста, введите число. ")
            continue
        if user_otv == num1 + num2:
            print("правильно")
            pr_otv += 1
        else:
            print("неправильно")
            npr_otv += 1
    print(f"игра окончена. правельных ответов: {pr_otv}")
mat_game()