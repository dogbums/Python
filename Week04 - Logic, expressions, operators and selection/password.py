# Program that prompts password, then accepts correct password ignoring case

askpassword = input ("Please enter your password: ")

askpassword = str.lower(askpassword)

storedpassword = "numbnutz"

if (askpassword == storedpassword):
    print("Welcome")
else:
    print("Wrong password")