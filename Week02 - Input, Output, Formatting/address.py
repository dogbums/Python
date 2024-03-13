# Simple code that asks for input of an address then formats it correctly in output as desired 

surname = str(input("Please enter your surname: "))
housenumber = int(input("Please enter your house number: "))
roadname = str(input("Please enter your road name: "))
town = str(input("Please enter your town: "))

# print ("Mr and Mrs Windsor") 
# print ("1, The Mall")
# print ("London")

print (f"Mr and Mrs {surname}") 
print (f"{housenumber}, {roadname}")
print (f"{town}")