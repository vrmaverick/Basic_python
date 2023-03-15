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