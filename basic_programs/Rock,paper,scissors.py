import random
def valid (v):
    if v>3 or v<1:
        print("Invalid choice")
        return 0
    else:
        return 1
def game(u,v):
    r=random.randint(1,3)
    print(r)
    if(u==3):
        print("User:Scissor")
        if(r==3):
            print("Computer:Scissor")
            w=0
        elif(r==2):
            print("Computer:paper")
            w=1
        else:
            print("Computer:rock")
            w=-1
    elif(u==2):
        print("User:Paper")
        if(r==3):
            print("Computer:Scissor")
            w=-1
        elif(r==2):
            print("Computer:paper")
            w=0
        else:
            print("Computer:rock")
            w=1
    else:
        print("User:Rock")
        if(r==3):
            print("Computer:Scissor")
            w=1
        elif(r==2):
            print("Computer:paper")
            w=-1
        else:
            print("Computer:rock")
            w=0
    if(w==0):
        return 0
    elif(w==1):
        return 1
    else:
        return -1
        
print("Rock......... Paper....... Scissor")
print("You have 5 turns against computer")
c=0
score=0
while c<5:
    l = {1:"Rock",
        2:"Paper",
        3:"Scisssor"}
    print(l)
    a = int(input("Enter Choice : "))
    v = valid(a)
    if(v==1):
        s=game(a,v)
        c=c+1
        score=s+score
    else:
        break
print("YOur score is :",score)

