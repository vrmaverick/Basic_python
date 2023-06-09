def hello():
    print("Hey!!!!!")


def call(funct):
    funct()


greet = hello
# del hello  # it deletes hello but not function we csn still point it by greet
print(greet())
print('$'*100)
call(hello)


def my_decorator(func):
    def func_wrap():
        print('^'*10)  # extra wrapping
        func()  # original function called
        print('v'*10)
    return func_wrap


# decorator called always decorators must be defined above .....a= my_decorator(hello)...a()
@my_decorator
def bye():
    print("Bye!!!!")

