from time import time


def performance(func):
    def wrap():
        t1 = time()
        func()
        t2 = time()
        print(f'Time taken = {t2-t1} ms')
    return wrap


@performance
def long():
    for i in range(0, 1000000000000000000000000000000000000):
        i*5


long()
