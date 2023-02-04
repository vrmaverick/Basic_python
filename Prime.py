def prime(n):
    p=0
    l=[1]
    for i in range(2,n-1) :
        if n%i==0:
            p=p+1
            l.append(i)
    l.append(n)
    if len(l)==2:
        print(n,"is a prime number")
        print("factors are :",end=" ")
        print(l)
    else:
        print(n,"is not a prime number")
        print("factors are :",end=" ")
        print(l)


print("Prime number checker")
n =int(input("Enter a  positive number : "))
if n<0 :
    print("Sorry the input should pe a postive number")
    print("Try Again !!!")
else:
    prime(n)




