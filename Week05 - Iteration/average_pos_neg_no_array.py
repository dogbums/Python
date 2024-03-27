print("Please input 10 whole numbers (can be either positive or negative, but not zero): ")

# Initialize sums and counts
sum_positive = 0
count_positive = 0
sum_negative = 0
count_negative = 0

# Input and process each number
for i in range(1, 11):
    number = int(input(f"Please enter the {i}{'st' if i == 1 else 'nd' if i == 2 else 'rd' if i == 3 else 'th'} whole number: "))
    
    if number > 0:
        sum_positive += number
        count_positive += 1
    else:
        sum_negative += number
        count_negative += 1

# Calculate and print the results
if count_positive > 0:
    average_of_pos = sum_positive / count_positive
    print("Sum of positives: {}".format(sum_positive))
    print(f"Average of positives: {average_of_pos}")
else:
    print("No positive numbers entered")

if count_negative > 0:
    average_of_neg = sum_negative / count_negative
    print("Sum of negatives: {}".format(sum_negative))
    print(f"Average of negatives: {average_of_neg}")
else:
    print("No negative numbers entered")