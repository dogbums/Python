# Calculating how many whole sweets can be shared between students

totalnumberofsweets = int(40)
numberofstudents = int(14)


sweetsforteacher = (totalnumberofsweets % numberofstudents)

sweetsforstudents = (totalnumberofsweets - sweetsforteacher)

sweetsperstudent = (sweetsforstudents / numberofstudents)

#totalsweetsforstudents = (totalnumberofsweets % numberofstudents)

#sweetsperstudent = (totalsweetsforstudents / 14)

#sweetsforteacher = (totalnumberofsweets - sweetsperstudent * 14)

#print(f"Number of sweets each: {sweetsperstudent}")

print(f"Sweets per student: {sweetsperstudent}")

print(f"Sweets left for teacher: {sweetsforteacher}")