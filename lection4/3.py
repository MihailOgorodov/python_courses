# 💡 Функция map() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с новыми объектами.
# list_1 = [x for x in range(1,30)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

import random

my_list = [random.randint(0, 20) for _ in range(10)]

data = '123 423 436 456 24 243 12 2 344 5 65 4 32'
print(data)

# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)


def where(f, col):
    return [x for x in col if f(x)]


res = map(int, my_list)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)