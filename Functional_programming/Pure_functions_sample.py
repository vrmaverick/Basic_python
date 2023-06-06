# new_list = [] #if defined outside and not in function it will change global variable thus not pure function
def mul_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list
# print(new_list)
print(mul_by_2([1, 2, 3]))
# print(new_list)
