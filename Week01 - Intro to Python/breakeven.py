# program to figure out how many products must be sold for a company to break even

fixedcosts = int(50000)
saleprice = int(40)
itemcost = int(20)

profitperitem = (saleprice - itemcost)

breakeven = (profitperitem / fixedcosts)

numberofitems = (fixedcosts / breakeven)


print (profitperitem)
print (breakeven)
print (numberofitems)