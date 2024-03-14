
BPS = 1

MBPS = BPS*1000000

MAX = 1000*MBPS

APPA = float (200000*BPS)

APPB = float (100000*BPS)

CURRENT = float (APPA + APPB)*200

NEWAPP = (350000*BPS)*200

LEFTOVER = (MAX-CURRENT)

NEWAVAIL = (LEFTOVER -NEWAPP)/1000000

print(f"Maximum network capacity: {MAX} bps")

print(f"Current network usage: {CURRENT} bps")

print(f"Current availability: {LEFTOVER} bps")

print(f"New application requirement: {NEWAPP} bps")

print(f"Bandwidth available after new app is installed {NEWAVAIL} Mbps")