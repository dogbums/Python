fixedcosts = (50000)
saleprice = (40)
itemcost = (20)

profitperitem = (saleprice - itemcost)

breakeven = (fixedcosts / profitperitem)

print (("Fixed costs: ") , fixedcosts)
print (("Sale price for each item: ") + str(saleprice))
print (("Cost to produce each item: ") + str(itemcost))
print (("Profit per item: ") + str(profitperitem))
print (("Break even: ") + str(breakeven) , ("items"))