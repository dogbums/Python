# A program that calculates call charges

minutes =int(input("Please enter number of minutes: "))

callcharge = (minutes*0.15)

totalbill = (callcharge)*1.2

VAT = (callcharge)*0.2

print(f"Number of minutes used: {minutes}")

print(f"Basic call charge: £{callcharge:.2f}")

print(f"VAT due: £{VAT:.2f}")

print(f"Total bill: £{totalbill:.2f}")