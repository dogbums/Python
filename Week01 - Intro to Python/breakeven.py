# program to figure out how many products must be sold for a company to break even

fixedcosts = (50000)
saleprice = (40)
itemcost = (20)

profitperitem = (saleprice - itemcost)

breakeven = (fixedcosts / profitperitem)

numberofitems = (fixedcosts / breakeven)


print ("profit per item:") 
print (profitperitem)
print ("break even:")
print (breakeven)
print ("number of items which must be sold:")
print (numberofitems)