print("Please input 5 whole numbers (can be either positive or negative, but not zero): ")

positivelist = 0

negativelist = 0

wordList = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
for i in range (0, 10):
    num = int (input(f"Please enter the {wordList [i]} number: "))
    if num > 0:
        positivelist += num
    else:
        negativelist += num

print(f"Sum of positives: {positivelist}")
print(f"Sum of negatives: {negativelist}")