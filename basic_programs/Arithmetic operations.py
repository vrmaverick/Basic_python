def add_num(a,b):
    sum=a+b;
    return sum;

def sub_num(a,b):
    sub=a-b;
    return sub;

def mul_num(a,b):
    mul=a*b;
    return mul;


def div_num(a,b):
    di=a/b;
    return di;

num1=int(input("input the first number : "))
num2=int(input("input the second number :"))
ch=0
# ch = input("Enter : \n 1 for Addition \n 2 for Subtration \n 3 for Multiplication \n 4 for Division  \n 5 to Exit \n Input : ")
while(ch!=5):
    ch = input("Enter : \n 1 for Addition \n 2 for Subtration \n 3 for Multiplication \n 4 for Division  \n 5 to Exit \n Input : ")
    if ch == '1':
     print("The sum is",add_num(num1,num2))
    elif ch == '2':
     print("The subtraction is",sub_num(num1,num2))
    
    elif ch == '3':
     print("The multiplication is",mul_num(num1,num2))
    
    elif ch == '4':
     print("The Division is",div_num(num1,num2))
     
    elif ch == '5':
     print("Exit")
    else :
        print("Invalid Option!! ")

