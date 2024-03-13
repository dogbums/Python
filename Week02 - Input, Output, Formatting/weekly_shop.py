# A program designed to input and calculate the price of a weekly shop and display the total number of items as well as the 
# number of individual item and cost

# peaches = input("Enter number of peaches: ")
# beans = input("Enter number of cans of beans: ")
# chickenpieces = input("Enter number of packets of chicken pieces: ")
# socks = input("Enter number of pairs of socks: ")
# bottlesofwater = input("Enter number of bottles of water: ")

#REMOVE THIS AFTER DEVELOPMENT IS COMPLETE
peaches = "6"
beans = "5"
chickenpieces = "6"
socks = "3"
bottlesofwater = "2"

# priceofpeaches = input("Enter the price of a peach: ")
# priceofbeans = input("Enter the price of a can of beans: ")
# priceofchickenpieces = input ("Enter the price of a packet of chicken pieces: ")
# priceofsocks = input("Enter the price of a pair of socks: ")
# priceofbottlesofwater = input("Enter the price of a bottle of water: ")

#REMOVE THIS AFTER DEVELOPMENT IS COMPLETE
peaches = "6"
priceofpeaches = "0.60"
priceofbeans = "1"
priceofchickenpieces = "2.50"
priceofsocks = "4.00"
priceofbottlesofwater = "1.50"

totalnumberofitems = (int(peaches) + int(beans) + int(chickenpieces) + int(socks) + int(bottlesofwater))

totalpriceofitems = (float(priceofpeaches) + float(priceofbeans) + float(priceofchickenpieces) + float(priceofsocks) + float(priceofbottlesofwater))

print(f"Peaches \n-how many? {peaches}\n-price? {priceofpeaches}")
print(f"Beans \n-how many? {beans}\n-price? {priceofbeans}")
print(f"Chicken \n-how many? {chickenpieces}\n-price? {priceofchickenpieces}")
print(f"Socks \n-how many? {socks}\n-price? {priceofsocks}")
print(f"Bottles of water \n-how many? {bottlesofwater}\n-price? {priceofbottlesofwater}")

print(f"Total number of items purchased: {totalnumberofitems}")
print(f"Your weekly shop cost: {totalpriceofitems:.2f}")