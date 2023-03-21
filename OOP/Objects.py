class Player:
    #Class Object attribute .........it is static
    Membership = True

    def __init__(self, name, year):
        self.name = name
        self.yearrrr = year
    def run(self):
        print("Running")
        return 0 #anything
    def shout(self):
        print(f'my name is {self.name}')#need to specify in curly space self.name to recognise

    @classmethod #decorator hai class methods ko intantiate karne ki jarurat nahi hoti
    def add(cls, num1, num2):#yaha cls hota hai self nahi cls is class
        return num1+num2
    @classmethod
    def create(cls,num1,num2):
        return cls('Bot', num1+num2)

obj1 = Player("vedant", 2003)#instantiate()
obj2 = Player("Ranade", 2023)#instantiate()
print(obj1)
print(obj1.name)
print(obj1.yearrrr)
print(type(obj1))


print(obj2.run())#when function does not return anything we get none
# help(list)#gives blueprint of class


print(obj2.Membership)#True it will exist for all objects Class object attribute is static
print(obj2.shout())


# print(obj1.add(2,8))#class method works on object or directly on class no need to instantiate
print(Player.add(2,8))#same results

#using class methods we can intsantiate a new object
bot = Player.create(1000,1023)
print(bot.yearrrr)
