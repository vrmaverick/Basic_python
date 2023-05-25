a = [15,12,56,69,99]#declaring lists
print(a)
print(a[2])#indexing
a = [26,'vedant','ranade',True]#diffrent data types in one list
print(a)
print(a[2])
a[2] = 12#index changing
print(a)
print( a [0:2])#slicing

amazon = ['notebooks','toys','electronics','food']
print(amazon[2])
amazon[2] = 'Playstation'
print(amazon[2])

print (amazon[1:]) #does not change original list
print(amazon)

amazon[0]='laptop'
new = amazon # same memory access shared
new[0]='Fridge'#amazon is also modified
print(amazon)

new2 = amazon[:]#we assign a diffrent copy
new2[0]='Heater'
print(amazon)
print(new2)
