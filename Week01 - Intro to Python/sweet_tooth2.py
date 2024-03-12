# Calculating how many whole sweets can be shared between students


def homonculous(totalnumberofsweets, numberofstudents):
    sweetsforteacher = (totalnumberofsweets % numberofstudents)
    sweetsforstudents = (totalnumberofsweets - sweetsforteacher)
    sweetsperstudent = (sweetsforstudents / numberofstudents)
    return sweetsperstudent , sweetsforteacher

#sweetsforteacher = (totalnumberofsweets % numberofstudents)

#sweetsforstudents = (totalnumberofsweets - sweetsforteacher)

#sweetsperstudent = (sweetsforstudents / numberofstudents)

while True:

   totalnumberofsweets = int(input("Input number of sweets"))
   numberofstudents = int(input("Input number of students"))

   result , result2 = homonculous(totalnumberofsweets , numberofstudents)


   print(f"Sweets per student: {result}")

   print(f"Sweets left for teacher: {result2}")