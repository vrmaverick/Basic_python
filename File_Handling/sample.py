my_file = open('Test.txt')
print(my_file)
print(my_file.read())
my_file.seek(10) # shifting cursor back
print(my_file.read())
my_file.seek(0)
# print(my_file.readline())
print(my_file.readlines())

