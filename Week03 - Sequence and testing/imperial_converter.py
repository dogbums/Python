import math

print("Please input height in feet and inches: ")

feet = int(input("Feet: "))
inches = int(input("Inches: "))

# 1 foot = 0.305 metres
# 1 inch = 0.025 metres

totalinches = (feet*12)+(inches)

centimetres = (totalinches*2.54)

print(centimetres)

# metres
# centimetres
# millimetres

# print(f"Kilometres: {kilometres:.6f}")

# print(f"Metres: {heightinmetres}")



