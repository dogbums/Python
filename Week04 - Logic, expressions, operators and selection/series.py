print("Please input 5 whole numbers (can be either positive or negative, but not zero): ")

num1 = int(input("Please enter the first whole number: "))
num2 = int(input("Please enter the second whole number: "))
num3 = int(input("Please enter the third whole number: "))
num4 = int(input("Please enter the fourth whole number: "))
num5 = int(input("Please enter the fifth whole number: "))

num1neg = (num1 or 0)
num1pos = (num1 or 0)
num2neg = (num2 or 0)
num2pos = (num2 or 0)
num3neg = (num3 or 0)
num3pos = (num3 or 0)
num4neg = (num4 or 0)
num4pos = (num4 or 0)
num5neg = (num5 or 0)
num5pos = (num5 or 0)

num1 = (num1pos or num1neg)
num2 = (num2pos or num2neg)
num3 = (num3pos or num3neg)
num4 = (num4pos or num4neg)
num5 = (num5pos or num5neg)

if (num1 > 0):
    num1pos = num1
else: num1pos = 0

if (num1 < 0):
    num1neg = (num1)

else: num1neg = 0

if (num2 > 0):
    num2pos = num2
else: num2pos = 0

if (num2 < 0):
    num2neg = (num2)

else: num2neg = 0

if (num3 > 0):
    num3pos = num3
else: num3pos = 0

if (num3 < 0):
    num3neg = (num3)

else: num3neg = 0

if (num4 > 0):
    num4pos = num4
else: num4pos = 0

if (num4 < 0):
    num4neg = (num4)

else: num4neg = 0

if (num5 > 0):
    num5pos = num5
else: num5pos = 0

if (num5 < 0):
    num5neg = (num5)

else: num5neg = 0

# if num1 == num1pos:
#     num1neg = 0
# else:
#     num1pos = 0

# if (num2 > 0):
#     num2 = (num2pos)
# else:
#     num2 = (num2neg)

# if num2 == num2pos:
#     num2neg = 0
# else:
#     num2pos = 0

# if (num3 > 0):
#     num3 = (num3pos)
# else:
#     num3 = (num3neg)

# if num3 == num3pos:
#     num3neg = 0
# else:
#     num3pos = 0

# if (num4 > 0):
#     num4 = (num4pos)
# else:
#     num4 = (num4neg)

# if num4 == num4pos:
#     num4neg = 0
# else:
#     num4pos = 0

# if (num5 > 0):
#     num5 = (num5pos)
# else:
#     num5 = (num5neg)

# if num5 == num5pos:
#     num5neg = 0
# else:
#     num5pos = 0

totalpos = (num1pos + num2pos + num3pos + num4pos + num5pos)

totalneg = (num1neg + num2neg + num3neg + num4neg + num5neg)

print(f"Sum of positive integers: {totalpos}")
      
print(f"Sum of negative integers: {totalneg}")

# # print("Sum of positive integers:" (positivenums))

# # print("Sum of negative integers: "(negativenums))