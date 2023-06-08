my_set = {char for char in 'maverick'}
print(my_set)
# expression for  param in iterable
new_set = {num*2 for num in range(1, 100, 2)}
print(new_set)
# display only even squares in range 0 to 100
se = {num**2 for num in range(0, 100) if num % 2 == 0}
print(se)
