# Calculating how many whole sweets can be shared between students

totalnumberofsweets = int(40)
numberofstudents = int(14)


sweetsforteacher = (totalnumberofsweets % numberofstudents)

sweetsforstudents = (totalnumberofsweets - sweetsforteacher)

sweetsperstudent = (sweetsforstudents / numberofstudents)


print(f"Sweets per student: {int(sweetsperstudent)}")

print(f"Sweets left for teacher: {sweetsforteacher}")