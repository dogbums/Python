# peaches = input()
# beans = input()
# chickenpieces = input()
# socks = input()
# bottlesofwater = input()

# input (f"Enter number of peaches: {peaches}")
# input (f"Enter number of cans of beans: {beans}")
# input (f"Enter number of packs of chicken pieces: {chickenpieces}")
# input (f"Enter number of pairs of socks: {socks}")
# input (f"Enter number of bottles of water: {bottlesofwater} ")

# print (f"Peaches {peaches}")

# number1 = input("Enter number 1: ")
# number2 = input("Enter number 2: ")
# total = int(number1) + int(number2) 
# print(total)

peaches = input("Enter number of peaches: ")
beans = input("Enter number of cans of beans: ")
chickenpieces = input("Enter number of packets of chicken pieces: ")
socks = input("Enter number of pairs of socks: ")
bottlesofwater = input("Enter number of bottles of water: ")

priceofpeaches = input("Enter the price of a peach: ")
priceofbeans = input("Enter the price of a can of beans: ")
priceofchickenpieces = input ("Enter the price of a packet of chicken pieces: ")
priceofsocks = input("Enter the price of a pair of socks: ")
priceofbottlesofwater = input("Enter the price of a bottle of water: ")

totalnumberofitems = (int(peaches) + int(beans) + int(chickenpieces) + int(socks) + int(bottlesofwater))

totalpriceofitems = (float(priceofpeaches) + float(priceofbeans) + float(priceofchickenpieces) + float(priceofsocks) + float(priceofbottlesofwater))

print(f"Peaches \n{peaches}")

print(totalnumberofitems)
print(totalpriceofitems)