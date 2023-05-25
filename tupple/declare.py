t1=(1,2,3,4,5)
print(t1)
# t1[0]=56 cannot modify tupple
# print(t1)
t2=()#empty
print(t2)
t3=("vedant",)#only single element
print(t3)
t4=("vedant","ranade",26,12)
print(t4)
# ..................................................................................
t = (1,2,3,4,5,6)
print(t[1:2])#single element
x,y,z,*other= t #unpacking
print(x)
print(y)
print(z)
print(other)
