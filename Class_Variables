class Employee :
    percent = 1.05 #class variable declared
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def raise_pay(self):
        self.pay=int(self.pay * self.percent) # Class variable called

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1.pay)
emp_1.raise_pay() #Method excecuted
print(emp_1.pay)
print(emp_2.pay)
# print(Employee.raise_pay()) #called via class so all objects will be raised
# print(emp_1.raise_pay()) #will return no value
# print(emp_2.raise_pay()) #will return no vale
emp_1.percent=1.80
print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)
emp_1.raise_pay() #Method excecuted
print(emp_1.pay)
