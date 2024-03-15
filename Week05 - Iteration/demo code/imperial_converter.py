go_again = True

while go_again:
    print("Enter height (feet then inches)")

    feet = int(input("Feet? "))
    inches = int(input("Inches? "))

    height = feet * 12 + inches

    centimetres = height * 2.54
    millimetres = centimetres * 10
    metres = centimetres / 100
    km = metres / 1000

    print(millimetres)
    print(centimetres)
    print(metres)
    print(km)

    again = input("Go again? ")
    if again == "n":
        go_again = False