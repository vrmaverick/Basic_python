dob=input("Enter date of birth in DDMMYYYY format : ")
year=int (dob[4:len(dob)])
cy=int(input("current year : "))
print( 'Your age is or going to turn '+ str(cy-year) + "this year" )

# without using any libraries
