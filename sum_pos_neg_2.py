print("Please input 5 whole numbers (can be either positive or negative, but not zero): ")

numberlist = []
wordList = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
for i in range (0, 10):
    num = int (input(f"Please enter the {wordList [i]} number: "))
    numberlist.append(num)

positivelist = 0

negativelist = 0

for i in range(0, len(numberlist)):
    r = numberlist[i]
    if r > 0:
        positivelist += r
    else:
        negativelist += r

print(f"Sum of positives: {positivelist}")
print(f"Sum of negatives: {negativelist}")