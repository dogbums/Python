print("Please input 5 whole numbers (can be either positive or negative, but not zero): ")

num1 = int(input("Please enter the first whole number: "))
num2 = int(input("Please enter the second whole number: "))
num3 = int(input("Please enter the third whole number: "))
num4 = int(input("Please enter the fourth whole number: "))
num5 = int(input("Please enter the fifth whole number: "))

num1neg = int
num1pos = int
num2neg = int
num2pos = int
num3neg = int
num3pos = int
num4neg = int
num4pos = int
num5neg = int
num5pos = int

if (num1 > 0):
    num1 = num1pos
else:
    num1 = num1neg

if (num2 > 0):
    num2 = num2pos
else:
    num2 = num2neg

if (num3 > 0):
    num3 = num3pos
else:
    num3 = num3neg

if (num4 > 0):
    num4 = num4pos
else:
    num4 = num4neg

if (num5 > 0):
    num5 = num5pos
else:
    num5 = num5neg

print (sum(f"{num1pos + num2pos + num3pos + num4pos + num5pos}"))

print (sum(f"{num1neg + num2neg + num3neg + num4neg + num5neg}"))

# print("Sum of positive integers:" (positivenums))

# print("Sum of negative integers: "(negativenums))