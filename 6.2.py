def delenie(num):
    return 100 / num
def main():
    try:
        znach = input("введите число на которое будите делить 100: ")
        num = float(znach)
        result = delenie(num)
        print(f"100 делиться на {num} равно {result}")
    except ValueError:
        print("Пожалуйста введите целое число.")
    except ZeroDivisionError:
        print("Деление на 0 неозможно.")
if __name__ == "__main__":