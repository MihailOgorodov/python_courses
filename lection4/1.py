# def f(x):
#     return x*x
# print(f(5))

# def calk1(a, b):
#     return a+b
# calk1 = lambda a, b: a + b


def calk2(a):
    return a * a


def math(op, x, y):
    print(op(x, y))


math(lambda a, b: a + b, 5, 2)
