words = []
print("введите слова, введите stop для завершения ввода")
while True:
    word = input()
    if word.lower() == "stop":
        break
    words.append(word)
result = ''.join(words)
print ("результат: ", result)