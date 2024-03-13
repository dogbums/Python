#program to breakdown how much paint is required to paint some walls

import math

areapaintedpercan = (5.1)

totalareapainted = ((40 * 3.4 * 2) + (30 * 3.4 *2))

numberofcans = math.ceil(totalareapainted / areapaintedpercan)

canarea = (0.15 * 0.15)

boxarea = (0.30 * 0.35)

totalcansinbox = math.floor(boxarea / canarea) * 2

totalfullboxes = math.floor(numberofcans / totalcansinbox)

cansnotinboxes = (numberofcans % totalcansinbox)

print (f"Total cans required: {numberofcans}")
print (f"Cans per box: {totalcansinbox}")
print (f"Full boxes: {totalfullboxes}")
print (f"Cans not in boxes: {cansnotinboxes}")