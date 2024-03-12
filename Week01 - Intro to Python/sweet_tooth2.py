# Calculating how many whole sweets can be shared between students

totalnumberofsweets = int(40)
numberofstudents = int(14)

def homonculous(totalnumberofsweets, numberofstudents):
    sweetsforteacher = (totalnumberofsweets % numberofstudents)
    sweetsforstudents = (totalnumberofsweets - sweetsforteacher)
    sweetsperstudent = (sweetsforstudents / numberofstudents)
    return sweetsperstudent , sweetsforteacher

#sweetsforteacher = (totalnumberofsweets % numberofstudents)

#sweetsforstudents = (totalnumberofsweets - sweetsforteacher)

#sweetsperstudent = (sweetsforstudents / numberofstudents)

result , result2 = homonculous(totalnumberofsweets , numberofstudents)



print(f"Sweets per student: {result}")

print(f"Sweets left for teacher: {result2}")