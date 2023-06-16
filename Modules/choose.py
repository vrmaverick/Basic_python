import random


def generate():
    n = []
    for i in range(2):
        num = random.randint(0, 9)
        n.append(num)
    return n
