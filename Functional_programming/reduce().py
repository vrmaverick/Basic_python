from functools import reduce
my_list = [1, 2, 3]
def accumulator(acc, item):
    return item*acc


print(reduce(accumulator, my_list, 100)) # used to reduce itrable to a specific value using any operations
