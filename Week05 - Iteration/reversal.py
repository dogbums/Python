number = input("Please enter a number between 1 and 11 digits long, or enter a negative number to quit: ")

dcount = 0

for d in number:

    dcount += 1

while dcount > 11:


        print("The number is invalid")
        break
    

if dcount <= 11:
    print("The number reversed is: ")
    print(number[::-1])