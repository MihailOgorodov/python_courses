import random

my_list = [random.randint(0, 20) for _ in range(10)]


# print(my_list)
# result = list()
#
# for i in my_list:
#     if i % 2 ==0:
#         result.append((i, i**2))
#
# print(result)

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


res = select(int, my_list)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)