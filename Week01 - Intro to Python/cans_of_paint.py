#program to breakdown how much paint is required to paint some walls

import math

areapaintedpercan = (5.1)

totalareapainted = ((40 * 3.4 * 2) + (30 * 3.4 *2))

numberofcans = math.ceil(totalareapainted / areapaintedpercan)

canarea = (0.15 * 0.15 * 0.30)

boxarea = (0.30 * 0.35 * 0.60)

totalcansinbox = (boxarea / canarea)

print (totalareapainted)
print (totalcansinbox)
print (numberofcans)