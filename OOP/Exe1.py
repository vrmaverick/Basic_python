#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
# 1 Instantiate the Cat object with 3 cats


cat1 = Cat('Aman', 7)
cat2 = Cat('Baman', 10)
cat3 = Cat('Chaman', 6)

# 2 Create a function that finds the oldest cat
def old(age1,age2,age3):
    if age1>age2:
        pass
    else:
        age1 = age2
    if(age1 > age3):
        pass
    else:
        age1=age3
    return age1
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in


o = old(cat1.age, cat2.age, cat3.age)
print(o)