# Calculating how many whole sweets can be shared between students

totalnumberofsweets = (40)
numberofstudents = (14)

sweetsperstudent = (40 % 4)

sweetsforteacher = (totalnumberofsweets - sweetsperstudent * 14)

print(f"Number of sweets each: {sweetsperstudent}")

print(f"Sweets left for teacher: {sweetsforteacher}")