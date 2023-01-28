age = int(input("Enter your age : "))
if(age<18 or age>55):
    print("cannot drive")
    if(age<18):
        print("you are",age,"and underage")
    else:
        print("take a medical checkup first as your age is",age)
else:
    print("allowed to drive")
