a = [26,12,2003,56,79,69,88,100]#it must be same data type
print("unsorted : ")
print(a)#does not concatinate list
a.sort()#modifies a does not return
print("sorted :")
print(a)
#.........................................
# new = sorted(a)........creates a copy of a and then sorts copy
# print(new)
# print(a) does not affect in sorted () function

a.reverse()
print("reverse : ") #decending order
print(a)


#adding

a.append(100)#adds 100 at end of list
print("100 is appended at end : ")
print(a)
a.insert(0,544)#insert 544 at 0th index.....l1.insert(index,value)
print("at 0th index 545 is added in list : ")
print(a)
a.insert(100,689)#last position as there are no 100 elements
print(a)
a.extend([100,200,300,400,500])
print(a)

c=a.index(200)
print(c) #returns index of which the first itself occurs
print(a.index(200,2,100))#start from index 2 to index 99 but there is no index 99 so till end of list.....gives error if not found
print(200 in a[11:])

c=a.count(100)
print (c)

#removing
b= a.pop(0) #returns popped value
print("0th index poped : ",b)
print(a) #removes that value from list
a.remove(100) #returns nothing 
print("100 is removed : ")
print(a)

x=str(a)
s = ' '
n =s.join(x) #joins  list using any string and returns new string .........only works on strings
print(n)
print (x)
# ....................................string unpacking
p,q,r,*other,z,y = [26,12,2003,56,79,69,88,100]
print(p)
print(q)
print(r)
print(other) #remaining list
print(z)
print(y)

