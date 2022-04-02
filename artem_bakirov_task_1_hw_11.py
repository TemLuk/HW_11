# Пример 1
def fun1(x):
    s = 1
    for i in range(1, x):
        yield i ** 2 + s
        s += 1


a = fun1(10)
for n in a:
    print(n)


# Пример 2
def fun2(x):
    for i in x:
        yield i**2


a = fun2([2, 4, 7, 10, 3])
for i in a:
    print(i)


# Пример 2
def fun3():
    n = 1
    while True:
        yield n*4
        n += 1

gen1 = fun3()
for i in gen1:
    print(i)
    if i > 40:
        gen1.throw(Exception('STOP!'))
