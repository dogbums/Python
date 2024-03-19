# A program that rolls two "dice" until they match

import random

dice1 = random.randint(1, 6)

dice2 = random.randint(1, 6)

if dice1 != dice2:
    print(f"No match {dice1, dice2}")
else:
    print (f"Match! {dice1, dice2}")

