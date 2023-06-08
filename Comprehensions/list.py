my_list = [char for char in 'maverick']
print(my_list)
# expression for  param in iterable
new_list = [num*2 for num in range(1, 100, 2)]
print(new_list)
# display only even squares in range 0 to 100
li = [num**2 for num in range(0, 100) if num % 2 == 0]
print(li)
