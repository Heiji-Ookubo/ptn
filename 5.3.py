def rare_word(word):
    if "ф" in word:
        return "ого! это редкое слово!"
    else:
        return "это не редкое слово"
user_vvod = input("введите слово: ")
res = rare_word(user_vvod)
print(res)
