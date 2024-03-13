u = input("Enter initial velocity: ")
t = input("Enter time: ")
a = input("Enter acceleration: ")

# UT = (initial_velocity * time)
# T2 = (time * time)
# AT2 = (acceleration * T2)
# S = (UT + (0.5 * AT2))

S = (u*t) + (0.5*a*(t*t))


print(S)