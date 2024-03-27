# number = input("Please enter a number between 1 and 11 digits long, or enter a negative number to quit: ")

# dcount = 0

# for d in number:

#     if d == "-":
#          break

#     else: dcount += 1
    

# while dcount > 11:


#         print("The number is invalid")
#         break
    

# if dcount <= 11:
#         print("The number reversed is: ")
#         print(number[::-1])

number = int(input("Please enter a number between 2 and 11 digits long, or enter a negative number to quit: "))

rev = 0

# while number < 0:
#       print("Invalid number")
#       number = int(input("Please enter a number between 2 and 11 digits long, or enter a negative number to quit: "))

while number > 9:
     rev = rev * 10 + (number % 10)
     number = number // 10
print(f"Number reversed: {rev}")

if number < 10:
       print("Invalid number")