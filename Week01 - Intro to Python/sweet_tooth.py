# Calculating how many whole sweets can be shared between students

totalnumberofsweets = (40)
numberofstudents = (14)


sweetsforteacher = (totalnumberofsweets % numberofstudents)

sweetsforstudents = (totalnumberofsweets - sweetsforteacher)

sweetsperstudent = (sweetsforstudents / numberofstudents)


print(f"Sweets per student: {int(sweetsperstudent)}")

print(f"Sweets left for teacher: {sweetsforteacher}")