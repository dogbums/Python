number = int(input("Please enter a whole number between 1 and 7: "))

match number:
    case 1:
        print("One for sorrow")
    case 2:
        print("Two for joy")
    case 3:
        print("Three for a girl")
    case 4:
        print("Four for a boy")
    case 5:
        print("Five for silver")
    case 6:
        print("Six for gold")
    case 7:
        print("Seven for a secret")
    case _:
        print("Not a permitted number")
