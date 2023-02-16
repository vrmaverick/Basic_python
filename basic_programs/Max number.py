def maxx(x,y,z):
    if (x>y):
        g=x
    else:
        g=y
    if (g>z):
        return g
    else:
        return z
print("Enter three numbers : ")
a=int(input("enter first number : "))
b=int(input("enter second number : "))
c=int(input("enter third number : "))
p=maxx(a,b,c)
print("Greatest value is : ",p)
