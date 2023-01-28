v = int(input("Enter howw many fibo numbers from series you want : "))
# print(type(v))
print("fibonacci series of ",v,"elements is :")
a = 0
b = 1
print(a,end="  ")
print(b,end="  ")
c = 0
i = 0
while(i<(v-2)):
    c = a + b
    print(c,end="  ")
    a = b
    b = c
    i = i + 1
