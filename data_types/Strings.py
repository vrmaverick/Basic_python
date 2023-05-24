Username = "VEDANT"
password = 'MAVERICK'
EMOJI = '''

O   O
_____



'''
merge = Username+password #no space
print(merge)

a = 100
b = str(a)
c = int (b)
print(type(b))
print(type(c))

name = input("enter your name ")
age = int (input("enter your age "))
city = input("enter your city ")

print('HIII'+ name+ ' your age is '+str(age)+'\n\tIt\'s sunny outside in '+ city)#normal
print(f'HIII {name} your age is {age}\n\tIt\'s sunny outside in {city}')#formatted
print('hii {new_name} your age is {0} it is to cold outside in {1}'.format(age,city,new_name='bot'))

# STRING MANIPULATION
s = "0123456789"
#+ve index 0123.....
#-ve index -9-8-7........
# [start:end:step],default 0
#end -1 tak
print(s[3])
print(s[3:])
print(s[3:8])
print(s[3:9:2])
print(s[::2])
print(s[::-1])
print(s[-2:-9:-2])


qoute = 'Honesty is best policy'
print(len(qoute))
print(qoute.capitalize())
print(qoute.upper())
print(qoute.find('be'))
print(qoute.replace('is ','not a '))
print(qoute) #immutable 
