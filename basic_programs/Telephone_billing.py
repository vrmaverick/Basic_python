def billing (no) :
    if no<=100:
        return 200
    elif no<=150:
        c = no-100
        return 200+(c*0.6)
    elif no<=200 :
         c = no-150
         return 230+(c*0.5)
    else:
        c = no-200
        return 255+(c*0.4)
number=int(input("Enter number of calls : "))
cost=billing(number)
print("Your bill is:Rs",cost)
