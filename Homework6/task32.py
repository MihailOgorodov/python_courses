# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

list_1 = [random.randint(-50, 50) for _ in range(10)]

min_value = int(input('Введите минимальное значение диапазона чисел: '))
max_value = int(input('Введите максимальное значение диапазона чисел: '))
print(list_1)

result_list = []
if max_value >= min_value:
    for i in range(len(list_1)):
        if min_value <= list_1[i] <= max_value:
            result_list.append(i)

print(result_list)
