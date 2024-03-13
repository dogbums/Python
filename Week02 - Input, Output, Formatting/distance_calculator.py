u = float(input("Enter initial velocity: "))
t = float(input("Enter time: "))
a = float(input("Enter acceleration: "))

# UT = (initial_velocity * time)
# T2 = (time * time)
# AT2 = (acceleration * T2)
# S = (UT + (0.5 * AT2))

S = (u*t) + (0.5*a*(t*t))


print(f"Distance in metres: {S}")