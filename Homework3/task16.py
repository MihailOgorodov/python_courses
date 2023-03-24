#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# import random
# count_list = int(input('Введите количество элементов: '))
# first_list = [random.randint(1,20) for i in range(count_list)]
# print(*first_list)
# number = int(input('Введите число: '))
# count = 0
# for i in range(len(first_list)):
#     if first_list[i] == number:
#         count += 1
# print(f'Число {number} встречается {count} раз')

import random
count_list = int(input('Введите количество элементов: '))
first_list = [random.randint(0,20) for _ in range(count_list)]
print(first_list)
number = int(input('Введите число: '))
print(f'Число {number} встречается в списке {first_list.count(number)} раз')
