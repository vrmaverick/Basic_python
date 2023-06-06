my_list = [1, 2, 3]


def mul_by_2(item):
    # def mul_by_2(li):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list
    return item*2


# returns an object we dont require iteration in functions
print(map(mul_by_2, my_list))
print(list(map(mul_by_2, my_list)))
print(my_list)  # my list does not change thus it does not effect others
