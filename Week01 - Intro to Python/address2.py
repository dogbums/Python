# Simple code that asks for input of an address then formats it correctly in output as desired 

surname = str(input("Please enter your surname: "))
housenumber = int(input("Please enter your house number: "))
roadname = str(input("Please enter your road name: "))
town = str(input("Please enter your town: "))

#print (surname) 
#print (housenumber , end="") , print (", " , end="") , print (roadname)
#print (town)

print (surname + "\n" + str(housenumber) + ", " + roadname + "\n" +town )