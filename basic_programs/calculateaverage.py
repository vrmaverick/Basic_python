def perc(mar) :
# def perc(*mar)://arbitary number or n number of arguments
# def my_function(marks = [15,14,23,45,50]):#default parameters
    s = sum(mar)#s is a parameter
    print(s)
    s = (s/500)*100
    print ("The calculated percentage of the following ",mar," is ",s)
    return s
def grade(g) :
    if(g>90):
        return 'A'
    elif(g>75):
        return 'B'
    elif(g>60):
        return 'C'
    elif(g>45):
        return 'D'
    elif(g>32):
        return 'E'
    else
        return 'F'
        print("You have Failed in the test")
        
print("This is a percentage % calculator")
marks = []
sub = []
m = 0
for i in range(5):
    m = input("Enter 5 subjects")
    sub.append(m)
print(sub)
for i in range(5):
    m = int(input("Enter Marks of ",sub[i]," : "))
    marks.append(m)
p=perc(marks)
gra=grade(p)
print("Grade:",gra)

# perc(1....,2....,3....,) n arguments passed
# s = sum(marks)
    
