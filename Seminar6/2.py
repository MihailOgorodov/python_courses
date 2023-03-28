# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного
import random

my_list = [random.randint(0, 20) for _ in range(10)]
print(my_list)
count = 0
size = len(my_list)
for i in range(size):  # закольцевать список с помощью длины листа size = len(my_list)
    if my_list[(i - 1) % size] < my_list[i % size] > my_list[(i + 1) % size]:
        count += 1
print(f'Количество элементов, у которых оба соседних элемента меньше данного - {count}')
