# calculate the average of four numbers

running_total = 0

for num in range(1, 5):
    running_total += int(input("Enter integer {}: ".format(num)))

avg = running_total / 4

print("Average is: " + str(avg))
