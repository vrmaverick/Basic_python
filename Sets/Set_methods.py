my_list=[1,2,3,4,5,5,5,6,6,7,4,3,6,4,]
my_set=set(my_list)
new_set={100,99,98,97,96,6,7,4,2,5,6}
print(my_set.intersection(new_set))
print(my_set.isdisjoint(new_set))
print(my_set|new_set)
print(my_set.difference(new_set))
print(my_set) #not modified
print(my_set.difference_update(new_set))#none
print(my_set)
print(my_set.discard(5)) #none
print(my_set)
