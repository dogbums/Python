# A program that rolls two "dice" until they match

# import random



# dice1 = random.randint(1, 6)

# dice2 = random.randint(1, 6)

# turn = 1

# print(f"{dice1}, {dice2}")


# while dice1 != dice2:
#     turn 
#     print(f"No match {dice1, dice2}")
# else:
#     print(f"Match! {dice1, dice2}")

import random

dice1 = random.randint(1, 6)

dice2 = random.randint(1, 6)

turns = 0

while dice1 != dice2:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 == dice2:
        print(f"Match! {dice1, dice2}")
    else:
        print(f"No match: {dice1, dice2}")
    turns += 1
print(f"Number of throws until match: {turns}")