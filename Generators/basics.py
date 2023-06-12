def generator(num):
    for i in range(num):
        yield i


for g in generator(100):
    print(g)
l = generator(1000)
next(l)
next(l)
next(l)
next(l)
next(l)
next(l)
print(next(l))
