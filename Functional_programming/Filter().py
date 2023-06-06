my_list = [1, 2, 3]


def mul_by_2(item):
    # def mul_by_2(li):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list
    return item*2


def only_odd(item):
    return item % 2 != 0  # returns true or false


print(filter(only_odd, my_list))  # it is an object
# prints only those items which satisfies condition
print(list(filter(only_odd, my_list)))
print(my_list)  # does not modify original list


new_list = filter(only_odd, my_list)
print(list(map(mul_by_2, new_list)))
