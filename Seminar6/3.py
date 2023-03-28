# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
import random

my_list = [random.randint(0, 20) for _ in range(10)]
print(my_list)
dict = {}
for i in my_list:
    dict[i] = dict.get(i, 0) + 1

print(dict)
sum_count = 0
for key, value in dict.items():
    sum_count += value // 2
print(f'Равных пар = {sum_count}')
