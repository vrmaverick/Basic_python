import re
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password_pattern = re.compile(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}\d$")
print("For Signup Into New Account")
while True:
    email = input("Enter you email address : ")
    a = pattern.search(email)
    if a:
        print("It is a valid email procceed to set password ...")
        break
    else:
        print("Please try again not valid email")
while True:
    password = input("Enter a Strong Password with atleast 8 Charecters,1 Caps,1 Symbol, and ends with any number : ")
    b = password_pattern.search(password)
    if b:
        print("Strong password for your account has been set !!!!")
        break
    else:
        print("Please complete the requirements")
