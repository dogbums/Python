import math

print("Please input height in feet and inches: ")

feet = float(input("Feet: "))
inches = float(input("Inches: "))

# 1 foot = 0.305 metres
# 1 inch = 0.025 metres

kilometres = (feet*0.305/1000)
# metres
# centimetres
# millimetres

print(f"Kilometres: "{kilometres:.6f}")



