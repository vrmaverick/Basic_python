my_list = [1, 2, 3]
our_list = [100, 200, 300]
their_list = [1000, 2000, 3000]


def mul_by_2(item):
    # def mul_by_2(li):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list
    return item*2


def only_odd(item):
    return item % 2 != 0  # returns true or false


print(zip(my_list, their_list, our_list))  # returns an object
print(list(zip(my_list, their_list, our_list)))  # zips iterables in tupple
print(my_list)  # original list does not change
sample_list = zip(my_list, their_list, our_list)


new_list = filter(only_odd, my_list)
print(list(map(mul_by_2, new_list)))
# n_list = filter(only_odd, sample_list)
# print(list(map(mul_by_2, n_list))) not supported
