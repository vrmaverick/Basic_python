class Super_list(list):
    def __len__(self):
        return 1000  # always return length of list as hidden


li = Super_list()
print(len(li))
li.append(45)
print(li[0])
print(issubclass(Super_list, list))
