print("Please input 5 whole numbers (can be either positive or negative, but not zero): ")

num1 = int(input("Please enter the first whole number: "))
num2 = int(input("Please enter the second whole number: "))
num3 = int(input("Please enter the third whole number: "))
num4 = int(input("Please enter the fourth whole number: "))
num5 = int(input("Please enter the fifth whole number: "))
num6 = int(input("Please enter the sixth whole number: "))
num7 = int(input("Please enter the seventh whole number: "))
num8 = int(input("Please enter the eight whole number: "))
num9 = int(input("Please enter the ninth whole number: "))
num10 = int(input("Please enter the tenth whole number: "))

number_list = num1, num2, num3, num4, num5, num6, num7, num8, num9, num10

positive_list = 0

negative_list = 0

for r in number_list:
    if r > 0:
        positive_list += r
    else:
        negative_list += r

average_of_pos = positive_list /5

average_of_neg = negative_list /5

print(f"Sum of positives: {positive_list}")
print(f"Average of positives: {average_of_pos}")
print(f"Sum of negatives: {negative_list}")
print(f"Average of negatives: {average_of_neg}")