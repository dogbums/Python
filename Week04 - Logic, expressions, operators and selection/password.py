# Program that prompts password, then accepts correct password ignoring case

askpassword = input ("Please enter your password: ")

askpassword = str.lower(askpassword)

if (askpassword) == str.lower("numbnutz"):
    print("Welcome")
else:
    print("Wrong password")