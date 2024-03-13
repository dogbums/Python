import math

print("Please input height in feet and inches: ")

feet = int(input("Feet: "))
inches = int(input("Inches: "))

# 1 foot = 0.305 metres
# 1 inch = 0.025 metres

totalinches = (feet*12)+(inches)

centimetres = (totalinches*2.54)

metres = (centimetres*100)

kilometres = (metres*1000)

millimetres = (centimetres/10)

centimetres = (centimetres)



print(f"Height in kilometres {kilometres}")
print(f"Height in metres {metres}")
print(f"Height in centimetres {centimetres}")
print(f"Height in millimetres {millimetres}")

# metres
# centimetres
# millimetres

# print(f"Kilometres: {kilometres:.6f}")

# print(f"Metres: {heightinmetres}")



