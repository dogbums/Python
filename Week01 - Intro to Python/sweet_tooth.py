# Calculating how many whole sweets can be shared between students

totalnumberofsweets = int(40)
numberofstudents = int(14)

sweetsperstudent = (totalnumberofsweets % numberofstudents)

sweetsforteacher = (totalnumberofsweets - sweetsperstudent * 14)

print(f"Number of sweets each: {sweetsperstudent}")

print(f"Sweets left for teacher: {sweetsforteacher}")