# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

count_list = int(input('Введите количество элементов: '))
first_list = [random.randint(1, 20) for i in range(count_list)]
print(*first_list)
number = int(input('Введите число: '))
temp = 0
find_num = [abs(first_list[i] - number) for i in range(len(first_list))]
print(first_list[find_num.index(min(find_num))])
