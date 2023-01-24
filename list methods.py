a = [26,12,2003,56,79,69,88]#it must be same data type
print("unsorted : ")
print(a)#does not concatinate list
a.sort()#modifies a does not return
print("sorted :")
print(a)
a.reverse()
print("reverse : ")
print(a)
a.append(100)#adds 100 at end of list
print("100 is appended at end : ")
print(a)
a.insert(0,544)#insert 544 at 0th index.....l1.insert(index,value)
print("at 0th index 545 is added in list : ")
print(a)
a.pop(0)
print("0th index poped : ")
print(a)
a.remove(100)
print("100 is removed : ")
print(a)

