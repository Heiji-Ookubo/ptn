def main ():
        password = input("введите пароль")
        confirm_password = input ("подтвердите пароль")
        if password == confirm_password:
         print ("пароль принят")
        else:
         print ("пароли не совпадают")
main()