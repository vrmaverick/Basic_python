class Student:
    def __init__(self,first,last,branch):#self is default rest all are attributes of class
        self.fname = first               # self.any_name = attribute_mentioned
        self.lname = last
        self.branch = branch # any name can be same as attribute
    def Fullname(self):#method
        return '{} {}'.format(self.fname, self.lname)

std1 = Student('Vedant','Ranade','AI & DS')
std2 = Student('Maverick','op','SHAIDS')
print(std1.fname)
print(std1.Fullname())
# print(Student.Fullname(std1))      also prints the same
# print(std2) #error



# alternate method but lenghty so we mention attributes in class
# std1.first='Vedant'
# std1.last='Ranade'
# std1.branch='AI & DS'
# std2.first='Maverick'
# std2.last='op'
# std2.branch='SHAIDS'
# print(std1.first)
# print(std2.branch)
