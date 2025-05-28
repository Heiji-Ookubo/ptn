def tip_mesta(mesto):
    if mesto<1 or mesto>54:
        print("несуществующее место")
    else:
            if mesto in range(1, 10):
                print("верхнее купе")
            if mesto in range(10, 18):
                print("нижнее купе")
            if mesto in range(19, 28):
                print("верхний плацкарт")
            if mesto in range(28, 37):
                print("нижний плацкарт")
            if mesto in range(37, 46):
                print("верхний плацкарт")
            if mesto in range(46, 55):
                print ("нижний плацкарт")
mesto = int(input("укажите место"))
tip_mesta(mesto)
