# program to figure out how many products must be sold for a company to break even

fixedcosts = (50000)
saleprice = (40)
itemcost = (20)

profitperitem = (saleprice - itemcost)

breakeven = (fixedcosts / profitperitem)

print (("Fixed costs: ") , fixedcosts)
print (("Sale price for each item: ") , saleprice)
print (("Cost to produce each item: ") , itemcost)
print (("Profit per item: ") , profitperitem)
print (("Break even:") , breakeven , ("items"))