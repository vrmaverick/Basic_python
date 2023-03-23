class Player:
    #Class Object attribute .........it is static
    Membership = True

    def __init__(self, name, year):
        self._name = name
        self._yearrrr = year
    def run(self):
        print("Running")
        return 0 #anything
    def shout(self):
        print(f'my name is {self._name}')#need to specify in curly space self.name to recognise

    @classmethod #decorator hai class methods ko intantiate karne ki jarurat nahi hoti
    def add(cls, num1, num2):#yaha cls hota hai self nahi cls is class
        return num1+num2

    @classmethod
    def create(cls,num1,num2):
        return cls('Bot', num1+num2)
    # static methods are same as class methods without cls components

obj1 = Player("vedant", 2003)#instantiate()
obj2 = Player("Ranade", 2023)#instantiate()
#abstraction
obj1.name ='Hello'
obj1.shout ='Overwritten'
print(obj1.shout)#Hello printed
# this gives a lot of access to users so we have to use private classes to restrict access and modify
# so we give underscore before so programers know not to touch it

