def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        yield a  # will return value of a and continue from here on
        temp = a
        a = b
        b = temp + b


for x in fibo(100):
    print(x)
