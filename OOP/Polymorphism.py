class User:
    def __init__(self,username,password):
        self.username= username
        self.password=password
    def login(self):
        print('logged in')
    def attack (self):
        print('Do nothing')


class Cavelry(User):
    def __init__(self, power, health):
        User.__init__(self,username = 'maverick',password='Lets gooo')
        self.power = power
        self.health = health
    def attack(self):
        User.attack(self)#parent class executed
        print(f'attacking with power {self.power}')
class Archer(User):
    def __init__(self, power, number):
        super().__init__(self, username='maverick', password='Lets gooo')
        self.power = power
        self.arrows = number

    def attack(self):
        print(f'attacking with arrows {self.arrows}')

arch1 = Archer('fire',10)
cava1 = Cavelry('Shells',100)
# print(cava1.attack())
# print(arch1.attack())
#we write a function which gives diffrent outputs always
def attacks (char):
    char.attack()#char is a object
attacks(arch1)#calling function
attacks(cava1)
print(arch1.username)