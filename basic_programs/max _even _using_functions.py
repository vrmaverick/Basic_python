def highest_even(li):
    max=0
    for c in li:
        if c%2==0 and c>max:
            max=c
    if max==0:
        return "No even number exist"
    return max
my_list=[]
count = int(input("enter number of items in the list : "))
for i in range(0,count):
    item = int(input("enter element : "))
    my_list.append(item)
print(f'your list is {my_list}')
print(f'Highest even number in the list is : {highest_even(my_list)}')
