from time import time


def performance(func):
    def wrap():
        t1 = time()
        func()
        t2 = time()
        print(f'Time taken = {t2-t1} ms')
    return wrap


@performance
def long1():
    print('without using list we can genrate a series of numbers')
    for i in range(100000):
        i*5


@performance
def long2():
    print('with using list ')
    for i in list(range(100000)):
        i*5


long1()
long2()
