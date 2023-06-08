my_list = [s for s in 'abcbdmnn']
# print(my_list)
duplicate = {value for value in my_list if my_list.count(value) > 1}
print(list(duplicate))
