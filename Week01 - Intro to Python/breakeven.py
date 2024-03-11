# program to figure out how many products must be sold for a company to break even

fixedcosts = (50000)
saleprice = (40)
itemcost = (20)

profitperitem = (saleprice - itemcost)

breakeven = (fixedcosts / profitperitem)

# print (("Fixed costs: ") , fixedcosts)
# print (("Sale price for each item: ") , saleprice)
# print (("Cost to produce each item: ") , itemcost)
# print (("Profit per item: ") , profitperitem)
# print (("Break even:") , breakeven , ("items"))

#String concatanation
# print (("Fixed costs: ") , fixedcosts)
# print (("Sale price for each item: ") + str(saleprice))
# print (("Cost to produce each item: ") + str(itemcost))
# print (("Profit per item: ") + str(profitperitem))
# print (("Break even: ") + str(breakeven) , ("items"))

#F-string method
print(f"Fixed costs: {fixedcosts}")
print(f"Sale price for each item: {saleprice}")
print(f"Cost to produce each item: {itemcost}")
print(f"Profit per item: {profitperitem}")
print(f"Break even: {breakeven} items")