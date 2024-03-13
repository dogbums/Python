rent = input("How much is your rent? ")
gas = input("How much is your gas? ")
electricity = input("How much is your electricity? ")
water = input("How much is your water? ")
counciltax = input("How much is your council tax? ")

total = (float(rent) + float(gas) + float(electricity) + float(water) + float(counciltax))

print(f"Rent per month: {rent}")
print(f"Gas payment per month: {gas}")
print(f"Electricity payment per month: {electricity}")
print(f"Water payment per month: {water}")
print(f"Council tax payment per month: {counciltax}")

print("Your total monthly expenses are:")
print(f"Rent:         £    {rent}")
print(f"Gas:          £    {gas}")
print(f"Electricity:  £    {electricity}")
print(f"Water:        £    {water}")
print(f"Council tax:  £    {counciltax}")

print("================================")
print(f"Total:        £    {total}")
print("================================")