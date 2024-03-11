# Program for measuring volume and surface area of a cuboid

height = int(input("Enter height: "))
width = int(input ("Enter width: "))
length = int(input ("Enter length: "))

volume = (height * width * length)
surface_area = ((height * width * 2) + (width * length * 2) + height * length * 2)

print (("Volume: ") , volume)

print (("Surface area: ") , surface_area)





