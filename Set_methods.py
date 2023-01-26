v = set()#set can also be declared this way
print(type(v))
#adding values inside set
v.add(26)
v.add(12)
v.add(2003)
v.add(26)#will not add repeated elements
v.add("maverick")
v.add(("tupple","can be added","but","not","list and dictionaries"))
print(v)
print(len(v))#prints length of sets
# v.remove(5)#removes 5 from set v it will throw error if not present
v.remove(2003)
print("now set is :",v)
print("............................................................")
p = v.pop()
print("popped element is ",p," popped from: ",v)
# v.clear() clears the whole set
