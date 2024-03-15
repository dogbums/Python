# Program that prompts password, then accepts correct password ignoring case

askpassword = input ("Please enter your password: ")

password = str.lower("numbnutz")

if password == ("numbnutz"):
    print("Welcome")
else:
    print("Wrong password")