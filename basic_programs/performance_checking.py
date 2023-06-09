from time import time
def performance(func):
    def wrap(*args, **kargs):
        t1 = time()
        func()
        t2 = time()
        print(f'Time taken = {t2-t1} ms')
        return wrap


@performance
def ti():
    for i in range(0, 10000000):
        i*5


a = ti()
