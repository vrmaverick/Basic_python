from functools import reduce
my_list = [2, 3, 5]
print(list(map(lambda item: item ** 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: item*acc, my_list, 10))
# lamda used for single use functions for memory efficiency but decrease readability
print("sum of squares of list items is : ")
print(reduce(lambda acc, item: acc+item, (map(lambda num: num**2, my_list)), 0))

 #lamda used for single use functions for memory efficiency but decrease readability
