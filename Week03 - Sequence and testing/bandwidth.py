
BPS = 1

MBPS = BPS/1000000

MAX = 1000/MBPS

APPA = 200000*BPS

APPB = 100000*BPS

CURRENT = (APPA + APPB)

NEWAPP = 350000*BPS

print(f"Maximum network capacity: {MAX}")

print(f"Current network usage: {APPA + APPB}")

print(f"Current availability: {MAX%CURRENT}")