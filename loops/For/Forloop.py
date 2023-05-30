ani=["lion","tiger","chipanzee","zebra","deer"]
for item in ani :
    print(item)
#Range function
sum = 0
for i in range(1,100,2):#range (start,end,step-size)
    sum = sum + i
print("sum is:",sum)#sum of 100 odd numbers

#in case of dictionaries we use few functions to iterate
#for loops cannot be used with integers as they are not iterable
user = {
    'name':'vedant',
    'age':19,
    'passed': True
}
for i in user.keys():
    print(i)
print('&'*80)
for i in user.items():
    key,value = i
    print(i)
    print(key,value)
    
    #reverse printing of list
    for _ in range(10,2,-1):
    print(_)
    print(list(range(5)))
