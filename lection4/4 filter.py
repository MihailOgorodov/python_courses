import random

data = [random.randint(0, 20) for _ in range(10)]
print(data)
res = list(filter(lambda x: x % 10 == 5, data))
print(res)


my_list = [random.randint(0, 20) for _ in range(10)]
print(my_list)
res1 = map(int, my_list)
res1 = filter(lambda x: x % 2 == 0, res1)
res1 = list(map(lambda x: (x, x**2), res1))
print(res1)