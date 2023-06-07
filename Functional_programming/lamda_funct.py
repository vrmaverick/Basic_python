from functools import reduce
my_list = [1, 2, 3]
print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: item*acc, my_list, 10))
 #lamda used for single use functions for memory efficiency but decrease readability
