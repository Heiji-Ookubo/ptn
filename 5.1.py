n=int(input("введите кол-во слова: "))
words = []
for i in range(n):
    word = input(f"Введите слово {i+1}: ")
    words.append(word)
result = ''.join(words)
print ("результат: ", result)