def vesgod(god):
        if god % 4 == 0 and god % 100 != 0 or god % 400 == 0:
            return True
        return False

def vesgodras(god):
    if vesgod(god):
        print (f"Год {god} високостный")
    else:
        print("год не високостный")
god_zn=int(input("укажите год: "))
vesgodras(god_zn)
