class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print('logged in')

    def attack(self):
        print('Do nothing')


class Cavelry(User):
    def __init__(self, power, health):
        User.__init__(self, username='maverick', password='Lets gooo')
        self.power = power
        self.health = health
        self.my_dict = {
            'name': 'Cavelery',
            'level': '90'
        }

    def attack(self):
        User.attack(self)  # parent class executed
        print(f'attacking with power {self.power}')

    def __str__(self):
        return f'{self.attack}'

    def __getitem__(self, i):
        return self.my_dict[i]


cava1 = Cavelry('Shells', 100)
print(dir(cava1))  # introspection
print(str(cava1))
print(cava1['level']) #get item
