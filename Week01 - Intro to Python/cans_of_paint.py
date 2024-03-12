#program to breakdown how much paint is required to paint some walls

import math

areapercan = (5.1)

totalareapainted = ((40 * 3.4 * 2) + (30 * 3.4 *2))

numberofcans = math.ceil(totalareapainted / areapercan)

boxarea = (0.60 * 0.35)

print (totalareapainted)
print (boxarea)
print (numberofcans)