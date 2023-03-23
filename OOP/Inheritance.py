class User:
    def login(self):
        print('logged in')


class Cavelry(User):
    def __init__(self, power, health):
        self.power = power
        self.health = health
    def attack(self):
        print(f'attacking with power {self.power}')
class Archer(User):
    def __init__(self, power, number):
        self.power = power
        self.arrows = number

    def attack(self):
        print(f'attacking with arrows {self.arrows}')

arch1 = Archer('fire',10)
print(arch1.attack())
print(arch1.login())
# isinstance(obj,class)
print(isinstance(arch1,Archer))
print(isinstance(arch1,User))
print(isinstance(arch1, object))