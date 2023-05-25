sets = {1,2,3,4,5,1}#sets are defined in curly brackets 
print(type(sets))
print(sets)#1 is repeated but still printed only once
print("......................................................................")
a = {}
print(type(a))#this syntax will create empty dictionary
#AN EMPTY SET CAN BE CREATED USING FOLLOWING SYNTAX
print("......................................................................")
b = set()#set can also be declared this way
print(type(b))
print("......................................................................")

my_list=[1,2,3,4,5,5,5,6,6,7,4,3,6,4,]
my_set=set(my_list)
print(my_set) #unique values
print(6 in my_set)
print(len(my_set))
print(len(my_list))
n = my_set.copy()
my_set.clear()
print(n)
print(my_set)
